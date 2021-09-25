#Step 15; Add redirect
from django.shortcuts import render,redirect
#Step 1; Import HttpResponse library for using it on two methods (index & staff): 
from django.http import HttpResponse
#Step 2; Import products
from .models import *
#Step 11; Import method login_required
from django.contrib.auth.decorators import login_required
#Step 15; Import all methods in forms @ homepage App
from .forms import *
#Step 16; Import Users
from django.contrib.auth.models import User



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
    #Step 15; Add quiryset for retrieve data
    items=Product.objects.all()
    #Step 15; Set quiryset include SQL statment
    #items=Product.objects.raw('SELECT * from homepage_product WHERE category = "food"')
    #Step 15; Add filtration
    #items=Product.objects.filter(category="food")
    #Step 15; Add count
    counts=Product.objects.count()

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_products')
    else:
        form=ProductForm()

    context={
        #Step 15; the name of "kokos" is the object will be pass into WebPage.html linked with quiryset "items"
        'kokos':items,
        #Step 15; Test count for objects
        'count_no':counts,
        'form':form,
    }
    return render(request, 'dashboard/products.html', context)

#Step 15; Create two methods for "delete" & "update" product
@login_required
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard_products')
    context={
        'items':item
    }
    #Step 15; you can remove context from this method
    return render(request,'dashboard/products_delete.html',context)

@login_required
def product_update(request,pk):
    item=Product.objects.get(id=pk)
    
    if request.method=='POST':
        form=ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard_products')
    else:
        form=ProductForm(instance=item)
    context={
        'items':item,
        'form':form,
    }

    return render(request,'dashboard/products_update.html',context)

#Step 16; Create two methods for "Staff" & "Details" product
@login_required
def staff(request):
    staffs=User.objects.all()

    context={
        'staffs':staffs,
    }
    return render(request,'dashboard/staff.html', context)

@login_required
def staff_details(request,pk):
    detailStaff=User.objects.get(id=pk)

    context={
        'detailStaffs':detailStaff,
    }
    return render(request, 'dashboard/staff_detail.html', context)

#Step 11; Set validation requied login
#@login_required(login_url='user_login')
#Step 11; Add LOGIN_URL ='user_login' at setting.py then write views.py the folloing:
@login_required
def orders(request):
    allOrders=Order.objects.all()

    context={
        'allOrders':allOrders,
    }
    return render(request, 'dashboard/orders.html', context)


