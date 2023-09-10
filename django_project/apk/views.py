from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>............Hello this is django classs............</h1>')


def index(request):
    return render(request, 'index.html')
    


def furniture(request):
    return render(request, 'furniture.html')


def products(request):
    return render(request, 'products.html')


def accessories(request):
    return render(request, 'accessories.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        check = Customer.objects.create(
            email=email, password=password, confirmpassword=confirmpassword)
        return HttpResponse('Registration successful...')
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def cart(request):
    return render(request, 'cart.html')


def singleproduct(request):
    return render(request, 'singleproduct.html')


def loginn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        check = Customer.objects.filter(email=email, password=password).first()
        if check is not None:
            request.session['email'] = email
            request.session['userid'] = check.id
            messages.success(request, 'Login successful!')
            return HttpResponse('Login successful...')
        else:
            return HttpResponse('invalid registration')
    return redirect('login')


def logout(request):
    del request.session['email']
    del request.session['userid']
    messages.success(request, 'Logout successful!')
    # return render(request, 'index.html')
    return HttpResponse('Logout successful')
