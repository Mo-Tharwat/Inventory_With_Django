#Step 9; Create a new form for models ==> User & forms ==> UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#Step 14; import these class's from form & import profile from models
from .models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #Step 9; Select some fields from '__all__'
        fields = ['username', 'password1','password2','email']

#Step 14; Create two methods for (UserUpdateForm & ProfileUpdateForm)
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','phone','image']