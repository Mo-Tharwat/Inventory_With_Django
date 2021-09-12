#Step 9; Create a new form for models ==> User & forms ==> UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #Step 9; Select some fields from '__all__'
        fields = ['username', 'password1','password2','email']
