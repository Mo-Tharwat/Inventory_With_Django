from django.shortcuts import render
#Step 1; Import HttpResponse library for using it on two methods (index & staff): 
from django.http import HttpResponse
#Step 2; Import products
from .models import *
#Step 11; Import method login_required
from django.contrib.auth.decorators import login_required


# Create your views here.

"""
#Step 1; Create two methods:
# this is the first method
def index(request):
    return HttpResponse('Hello World, from index')

# this is the second method
def staff(request):
    return HttpResponse('Hello World, from staff')
"""

#Step 2; Create two mentods using render with templates files
#Step 3; Add the new path of dashboard/template after movied these file on dashboard

#Step 11; Set validation requied login
#@login_required(login_url='user_login')
#Step 11; Add LOGIN_URL ='user_login' at setting.py then write views.py the folloing:
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

#Step 11; Set validation requied login
#@login_required(login_url='user_login')
#Step 11; Add LOGIN_URL ='user_login' at setting.py then write views.py the folloing:
@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

#Step 4; Create two mentods for products & orders
#Step 11; Set validation requied login
#@login_required(login_url='user_login')
#Step 11; Add LOGIN_URL ='user_login' at setting.py then write views.py the folloing:
@login_required
def products(request):
    return render(request, 'dashboard/products.html')

#Step 11; Set validation requied login
#@login_required(login_url='user_login')
#Step 11; Add LOGIN_URL ='user_login' at setting.py then write views.py the folloing:
@login_required
def orders(request):
    return render(request, 'dashboard/orders.html')


