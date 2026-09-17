from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterForm, UserLoginForm
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

@login_required(login_url='login')
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    products = Product.objects.all()
    return render(request,'home.html', {'products':products})


class Register_view(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        form = UserRegisterForm()
        return render(request, "Register.html", {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        return render(request, 'Register.html', {'form': form})
   
class Login_view(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        form = UserLoginForm()
        return render(request, "login.html", {'form' : form})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            messages.success(request, "Login successfully! Welcome back.")
            return redirect('home')
        return render(request, 'login.html', {'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('login')
    

        
               
        
             