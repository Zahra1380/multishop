from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'home'
urlpatterns = [
    # path('', cache_page(1*60)(views.Home.as_view()), name='home')
    path('', views.Home.as_view(), name='home')
]