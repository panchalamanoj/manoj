from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from .forms import CreateUserForm

def register(request):
       if  request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('')
       else:
           form = CreateUserForm()
       return render(request, 'register.html' , {'form': form})
               
def login(request):
    return render(request,'login.html')


def index (request):
    return render(request, 'index.html')
