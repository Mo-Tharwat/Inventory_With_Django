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


from django.contrib import admin
# Setp 1-2; Add include in the following to make mirror link between (the main of urls with the new extend file urls in the App)
from django.urls import path, include

# Step 9; Import the class of register
from user import views as user_views

#Step 10; Import auth_views class
from django.contrib.auth import views as auth_views

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
    #Step 10; Add in the pattern path 'dashboard' to move this main for login page
    path('dashboard/',include('homepage.urls')),
    #Step 8; Add the pattern of URL for register
    path('register/',user_views.register,name='user_register'),
    #Step 10; Add the pattern of URL for Login & Logout then Remove the pattern path 'login' to be main page in the site
    path('',auth_views.LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user_logout'),

]
