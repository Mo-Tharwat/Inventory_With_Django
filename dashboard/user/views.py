#Step 8; Add redirect with render
from django.shortcuts import render,redirect
#Step 8; import the UserCreationForm
from django.contrib.auth.forms import UserCreationForm
#Step 9; import all methods from form
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm 

# Create your views here.

#Step 8; Create a method for (register)
#Step 9; Replace the object from "UserCreationFrom" to be "CreationUserForm" ==> was created at forms.py
def register(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        #form=UserCreationForm()
        form=CreateUserForm()
    context={
        'form':form,
        }
    return render(request,'user/register.html',context)

#Step 12;Add method for user profile
def profile(request):
    return render(request,'user/profile.html')

#Step 14; Add method for user update profile (Edit the profile)
def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form =ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')
    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'user_form':user_form,
        'profile_form':profile_form, 
    }
    return render(request,'user/profile_update.html', context)