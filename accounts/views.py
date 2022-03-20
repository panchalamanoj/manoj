from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


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
    return render(request,'login.html')


def index (request):
    return render(request, 'index.html')
