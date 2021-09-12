#Step 8; Add redirect with render
from django.shortcuts import render,redirect
#Step 8; import the UserCreationForm
from django.contrib.auth.forms import UserCreationForm
#Step 9; import all methods from form
from .forms import *

# Create your views here.

#Step 8; Create a method for (register)
#Step 9; Replace the object from "UserCreationFrom" to be "CreationUserForm" ==> was created at forms.py
def register(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_index')
    else:
        #form=UserCreationForm()
        form=CreateUserForm()
    context={
        'form':form,
        }
    return render(request,'user/register.html',context)
