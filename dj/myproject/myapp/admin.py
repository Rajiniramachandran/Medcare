from django.contrib import admin
from django.forms import ModelForm
from .forms import MyForm
from .models import UserRegistration

# Register your models here.
@admin.register(UserRegistration)
class MyAdmin(admin.ModelAdmin):
    form=MyForm

