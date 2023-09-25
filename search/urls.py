from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('product-search/', views.SearchProduct.as_view(), name='product-search'),
]
