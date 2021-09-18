from django.contrib import admin
#Step 12; Add Model extends Users
from .models import *

# Register your models here.

admin.site.register(Profile),
