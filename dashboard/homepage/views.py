from django.shortcuts import render
#Step 1; Import HttpResponse library for using it on two methods (index & staff): 
from django.http import HttpResponse
#Step 2; Import 


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
def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

#Step 4; Create two mentods for products & orders
def products(request):
    return render(request, 'dashboard/products.html')

def orders(request):
    return render(request, 'dashboard/orders.html')


