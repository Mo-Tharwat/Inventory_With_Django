#Step 8; Add redirect with render
from django.shortcuts import render,redirect
#Step 8; import the UserCreationForm
from django.contrib.auth.forms import UserCreationForm
#Step 9; import all methods from form
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm 
#Step 11; Import method login_required
from django.contrib.auth.decorators import login_required
#Step 18; import message
from django.contrib import messages

# Create your views here.

#Step 8; Create a method for (register)
#Step 9; Replace the object from "UserCreationFrom" to be "CreationUserForm" ==> was created at forms.py
def register(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #Step 18;Create alert message
            create_register=form.cleaned_data.get('username')
            messages.success(request,f'This user "{create_register}" has been created successfully')
            #=====================Step 18.
            return redirect('user_login')
    else:
        #form=UserCreationForm()
        form=CreateUserForm()
    context={
        'form':form,
        }
    return render(request,'user/register.html',context)

#Step 12;Add method for user profile
@login_required
def profile(request):
    return render(request,'user/profile.html')

#Step 14; Add method for user update profile (Edit the profile)
@login_required
def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form =ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #Step 18;Create Alert message
            profile_name=user_form.cleaned_data.get('name')
            messages.success(request,f'Your account {profile_name} has been successfully')
            #=====================Step 18
            return redirect('user_profile')
    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'user_form':user_form,
        'profile_form':profile_form, 
    }
    return render(request,'user/profile_update.html', context)