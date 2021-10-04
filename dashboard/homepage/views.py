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
#step 18; Pop up message
from django.contrib import messages



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
#Step 16; Create objects in index method
#Step 17; Passing Order Form with the necessary validation
@login_required
def index(request):
    #Collect all data
    #orders=Order.objects.all()
    #Filter on login user
    orders=Order.objects.all()
    products=Product.objects.all()

    #Step 20; Count of objects staff
    staffsCounts=User.objects.count()
    productsCounts=Product.objects.count()
    ordersCounts=Order.objects.count()
    
    if request.method=="POST":
        form=OrderForm(request.POST)
        #item_id=Product.objects.get(id=pk)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.staff = request.user
            instance.save()
            #Step 18; Create a message
            order_product_name=form.cleaned_data.get('product')
            messages.success(request,f'Order of {order_product_name} has been created successfully')
            #==================Step 18.
            return redirect('dashboard_index')
    else:
        form=OrderForm()

    context = {
        'orders':orders,
        'form':form,
        'products':products,
        #Step 20; Passing the objects (staffCount, productsCounts, ordersCounts) to template
        'staffsCounts':staffsCounts,
        'productsCounts':productsCounts,
        'ordersCounts':ordersCounts, 
    }
    return render(request, 'dashboard/index.html',context)



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

    #Step 20; Count of objects staff
    staffsCounts=User.objects.all().count()
    productsCounts=Product.objects.all().count()
    ordersCounts=Order.objects.count()

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            #Step 18; Create a message           
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been created successfully')
            #==================Step 18.
            return redirect('dashboard_products')
    else:
        form=ProductForm()

    context={
        #Step 15; the name of "kokos" is the object will be pass into WebPage.html linked with quiryset "items"
        'kokos':items,

        #Step 15; Test count for objects
        'count_no':counts,
        'form':form,

        #Step 20; Passing the objects (staffCount, productsCounts, ordersCounts) to template
        'staffsCounts':staffsCounts,
        'productsCounts':productsCounts,
        'ordersCounts':ordersCounts, 
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

#Step 11; Set validation requied login
#@login_required(login_url='user_login')
#Step 11; Add LOGIN_URL ='user_login' at setting.py then write views.py the folloing:
#Step 16; Create two methods for "Staff" & "Details" product
@login_required
def staff(request):
    staffs=User.objects.all()

    #Step 20; Count of objects staff
    staffsCounts=User.objects.count()
    productsCounts=Product.objects.count()
    ordersCounts=Order.objects.count()

    context={
        'staffs':staffs,
        #Step 20; Passing the objects (staffCount, productsCounts, ordersCounts) to template
        'staffsCounts':staffsCounts,
        'productsCounts':productsCounts,
        'ordersCounts':ordersCounts,
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

#Step 16; Add queryset in the method orders
@login_required
def orders(request):
    allOrders=Order.objects.all()

    #Step 20; Count of objects staff
    staffsCounts=User.objects.count()
    productsCounts=Product.objects.count()
    ordersCounts=Order.objects.count()

    context={
        'allOrders':allOrders,
        #Step 20; Passing the objects (staffCount, productsCounts, ordersCounts) to template
        'staffsCounts':staffsCounts,
        'productsCounts':productsCounts,
        'ordersCounts':ordersCounts,
    }
    return render(request, 'dashboard/orders.html', context)


