from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('furniture/', views.furniture, name='furniture'),
    path('products/', views.products, name='products'),
    path('accessories/', views.accessories, name='accessories'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart'),
    path('singleproduct/', views.singleproduct, name='singleproduct'),
    path('loginn/',views.loginn,name='loginn'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('database/', views.database, name='database'),
    path('del_user/<id>', views.del_user, name='del_user'),
]
