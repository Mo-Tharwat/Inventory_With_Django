"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import homepage
from django.contrib import admin
# Setp 1-2; Add include in the following to make mirror link between (the main of urls with the new extend file urls in the App)
from django.urls import path, include

#Step 1; Add the following import all methods from App homepage: 
#--from homepage import views
#You Can use (from .import views) instead of (from homepage import views) as function views
#--from .import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Step 1; Add the pattern for path's:
    #--path('',views.index, name='index'),
    #--path('staff',views.staff, name='staff'),
    
    #Step 1-2; Add include another path:
    path('',include('homepage.urls')),
]
