from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import CreateUserForm 

def register(request):
       if  request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
       else:
           form = CreateUserForm()
       return render(request, 'register.html' , {'form': form})
               
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('')
              
    else:
        return render(request,'login.html')


def index (request):
    return render(request, 'index.html')
