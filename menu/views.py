from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def receita(request):
    return render(request, 'receita.html')