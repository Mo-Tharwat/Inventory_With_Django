from django.contrib import admin
#Step 5; Add the following library
from .models import * 
#Step 6; Add the following library (for return the group authentication group)
from django.contrib.auth.models import Group


# Register your models here.

#Step 6; rename the header of control panle
admin.site.site_header = "MTG-Inventory Dashboard"
#admin.site.site_title = "BeBo"

#Step 6; For management Class Product insert the following Class:
class ProductAdmin (admin.ModelAdmin):
    #You can control what the items will be appeared or sort these items as you need:
    list_display=('name','category','quantity')
    #You can add filtration for some items via tuples ("xxxxx",) or list []
    #list_filter=('category',)
    list_filter=['category']

#Step 5; register the model on Admin site
#Step 6; Add ProductAdmin on the admin.site.register
admin.site.register(Product, ProductAdmin)
#Step 7; Add register the model on admin site
admin.site.register(Order)


