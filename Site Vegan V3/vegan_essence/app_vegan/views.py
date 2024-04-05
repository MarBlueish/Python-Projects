from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def registo(request):
    return render(request,'registo/registo.html')

def login(request):
    return render(request,'login/login.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def menu(request):
    return render(request,'menu/menu.html')
