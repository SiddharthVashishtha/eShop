from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmpassword = models.CharField(max_length=200)
    profileimage = models.ImageField(upload_to='profile/', default='')
