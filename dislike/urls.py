from django.urls import path
from . import views
app_name = 'dislike'

urlpatterns = [
    path('product-dislike/<int:pk>', views.AddDisLikeProductView.as_view(), name='product-dislike'),
    path('detail-dislike/<int:pk>', views.DisLikeDetail.as_view(), name='detail-dislike'),
    path('product-dislike-list/', views.DisLike_list.as_view(), name='product-dislike-list'),
]
