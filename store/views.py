from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def fashion(request):
    return render(request,'fashion.html',{})