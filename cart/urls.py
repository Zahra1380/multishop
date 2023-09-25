from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('cart-detail', views.CartDetail.as_view(), name='cart-detail'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='add'),
    path('delete/<str:id>', views.CartDeleteView.as_view(), name='delete'),
    path('create-order/<int:pk>', views.CreateOrderView.as_view(), name='create-order'),
    path('order-detail/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('apply-discount/<int:pk>', views.ApplyDiscountView.as_view(), name='apply-discount'),
    path('send-request/<int:pk>', views.ApplyDiscountView.as_view(), name='send-request'),
    path('basket/', views.BasketView.as_view(), name='basket'),

]