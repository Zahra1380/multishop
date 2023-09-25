from django.urls import path
from . import views

app_name = 'like'

urlpatterns = [
    path('product-like/<int:pk>', views.AddLikeProductView.as_view(), name='product-like'),
    path('detail-like/<int:pk>', views.LikeDetail.as_view(), name='detail-like'),
    path('product-like-list/', views.Like_list.as_view(), name='product-like-list'),
]