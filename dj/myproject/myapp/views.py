from django.shortcuts import render,redirect
from django.forms import ModelForm
from .forms import MyForm
from .models import UserRegistration
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blogs(request):
    return render(request, 'blogs.html')

def book(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('next def name should be written inside this')
    else:
        form = MyForm()
    return render(request,'book.html', {'form': form})



   

def review(request):
    return render(request, 'review.html')

def service(request):
    return render(request, 'service.html')

def doctor(request):
    return render(request, 'doctor.html')

