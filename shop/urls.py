from django.urls import path
from .views import catalog, product_detail

urlpatterns = [
    path('', catalog, name='catalog'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
