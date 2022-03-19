from django.shortcuts import render,redirect
from django.http import HttpResponse
def register(request):
    return render(request, 'register.html')


	
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

	
