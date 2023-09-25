from django.shortcuts import render
from django.views import View
from product.models import Product
from product import models

# Create your views here.
class Home(View):
    def get(self, request):
        resent = Product.objects.all().order_by('-update')[:8]
        women = models.Gender.objects.get(gender='women')
        kids = models.Gender.objects.get(gender='kids')
        men = models.Gender.objects.get(gender='men')
        product = Product.objects.all()
        return render(request, 'HOME/index.html', {'resent_product': resent, 'men': men, 'women': women, 'kids': kids, 'product': product})