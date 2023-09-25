from django.urls import path
from . import views

app_name = 'Product'

urlpatterns = [
    path('product-detail/<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('navbar/', views.NavPartialView.as_view(), name='navbar'),
    path('category-item/', views.CategoryItemView.as_view(), name='category-item'),
    path('products/', views.ProductsList.as_view(), name='products-list'),
    path('products-sorting-price/', views.SortByPrice.as_view(), name='products-sorting-price'),
    path('products-sorting-create_date/', views.SortByCreateDate.as_view(), name='products-sorting-create_date'),
    path('products-showing-ten-item/', views.ShowingTenItem.as_view(), name='products-showing-ten-item'),
    path('products-showing-twenty-item/', views.ShowingTwentyItem.as_view(), name='products-showing-twenty-item'),
    path('products-showing-thirty-item/', views.ShowingThirtyItem.as_view(), name='products-showing-thirty-item'),
    path('special-products/', views.SpecialProductsList.as_view(), name='special-products-list'),
    path('women-products/', views.WomenProductsList.as_view(), name='women-products-list'),
    path('men-products/', views.MenProductsList.as_view(), name='men-products-list'),
    path('kids-products/', views.KidsProductsList.as_view(), name='kids-products-list'),
    path('share-product/', views.ShareProduct.as_view(), name='share-product'),
]
