from django.db import models

# Create your models here.
from django import forms


class UserRegistration(models.Model):
    username= models.CharField(max_length=50)
    usernumber = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=100)
    date = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.username