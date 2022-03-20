from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('')
    context = {}        
    return render(request,'login.html', context)


def index (request):
    return render(request, 'index.html')
