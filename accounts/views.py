from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth


from .forms import CreateUserForm
from django.contrib import messages

def register(request):
       if  request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'account was created for '+ user)
               return redirect('login')
       else:
           form = CreateUserForm()
       return render(request, 'register.html' , {'form': form})
               
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            redirect('')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
              
    else:
        return render(request,'login.html')


def index (request):
    return render(request, 'index.html')
