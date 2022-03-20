from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, password1=password1, first_name=first_name, last_name=last_name, email=email)
        user.save();
        print('user created')
        return redirect('home')

    else:
        return render(request, 'register.html')
               
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
              
    else:
        return render(request,'login.html')


def index (request):
    return render(request, 'index.html')
