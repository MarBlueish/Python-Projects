from django.shortcuts import render
from .models import Produto

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about/about.html')

def contact(request):
    return render(request,'contact/contact.html')

def guard(request):
    return render(request,'guard/guard.html')

def service(request):
    lista_produtos = {
        'products': Produto.objects.all()
    }
    return render(request,'service/service.html', lista_produtos)
