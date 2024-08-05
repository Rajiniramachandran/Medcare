"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import index
from myapp.views import about
from myapp.views import blogs
from myapp.views import book
from myapp.views import doctor
from myapp.views import review
from myapp.views import service
# from myapp.views import doctor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/about', about, name='about'),
    path('index/blogs', blogs, name='blogs'),
    path('index/book', book, name='book'),
    path('index/doctor', doctor, name='doctor'),
    path('index/review', review, name='review'),
    path('index/service', service, name='service'),
    
]
