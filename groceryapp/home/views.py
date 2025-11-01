from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,"index.html")

def shop(request):
    return render(request,'shop.html')

def shopdetail(request):
    return render(request,'shop-detail.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def Login(request):
    return render(request,'login.html')

def  checklogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
           login(request,user)
           return redirect('/dashboard')
        else:
             return redirect('/login/')

def dashboard(request):
    return render(request,'dashboard.html')   
    

    

