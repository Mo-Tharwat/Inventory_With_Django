#Step 1-2; Create new file as a name "urls.py" then add the following:
from django.urls import path
from .import views

#Step 1-2; Adding the following urlpatterns:
urlpatterns = [
    #Step 1-2; Adding the following path's:
    path('',views.index,name='dashboard_index'),
    path('staff/',views.staff,name='dashboard_staff'),
    #Step 4; Add two paths for methods (products & Orders)
    path('product/',views.products,name='dashboard_products'),
    path('product/<int:pk>/update/',views.product_update,name='dashboard_product_update'),
    path('product/<int:pk>/delete/',views.product_delete,name='dashboard_product_delete'),
    path('order/',views.orders,name='dashboard_orders'),
    
]