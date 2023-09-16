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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        check = Customer.objects.create(username=username, email=email, password=password, confirmpassword=confirmpassword)
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
            # return HttpResponse('Login successful...')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Invalid login credentials!')
            # return HttpResponse('invalid registration')
    return redirect('login')


def logout(request):
    del request.session['email']
    del request.session['userid']
    messages.success(request, 'Logout successful!')
    # return render(request, 'index.html')
    # return HttpResponse('Logout successful')
    return redirect('login')


def profile(request):
    if 'userid' in request.session:
        profile_data = Customer.objects.get(id=request.session['userid'])
        data = {'profile': profile_data}
        return render(request, 'profile.html', data)
    else:
        messages.add_message(request, messages.ERROR, 'Please login first!')
        return redirect('login')


def edit_profile(request):
    if 'userid' in request.session:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            profileimage = request.FILES['profileimage']

            data = Customer.objects.get(id=request.session['userid'])

            data.username = username
            data.email = email
            data.password = password
            data.profileimage = profileimage
            data.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully!")
            return redirect('profile')
        else:
            profile = Customer.objects.get(id=request.session['userid'])
            data = {'profile': profile, 'title': 'edit profile'}
            return render(request, 'edit_profile.html', data)
    else:
        messages.add_message(request, messages.ERROR, "Profile updated successfully!")
        return redirect('login')
    

def database(request):
    user_list = Customer.objects.all()
    data = {'user_list': user_list}
    return render(request, 'database.html', data) 

def del_user(request,id):
    check=Customer.objects.get(id=id)
    check.delete()
    messages.add_message(request, messages.SUCCESS, "Column deleted successfully!")
    return redirect('database')


