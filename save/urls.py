from django.urls import path
from . import views

app_name = 'save'

urlpatterns = [
    path('product-save/<int:pk>', views.AddSaveProductView.as_view(), name='product-save'),
    path('detail-save/<int:pk>', views.SaveDetail.as_view(), name='detail-save'),
    path('product-save-list/', views.Save_list.as_view(), name='product-save-list'),
]