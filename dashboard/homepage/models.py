from django.db import models
#Step 7; Add he following library (for return the User)
from django.contrib.auth.models import User


# Create your models here.

#Step 5; Add the following Class of Product:
CATEGORY =(
    ('Stationary','Stationary'),
    ('Electronices','Electronices'),
    ('food','food'),
)

class Product (models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        #The mentioned code make override on the name of class at "MTG-Inventory Dashboard\Homepage"
        verbose_name_plural = 'Product ***'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

#Step 7; Add the following Class of Order:
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=True)
    staff = models.ForeignKey(User, models.CASCADE, default=True)
    order_quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        #The mentioned code make override on the name of class at "MTG-Inventory Dashboard\Homepage"
        verbose_name_plural='Order ---'

    def __str__ (self):
        return f'{self.product} Ordered by {self.staff.username}'
