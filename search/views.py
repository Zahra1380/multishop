from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
# Create your views here.
class SearchProduct(ListView):
    template_name = 'search/search_page.html'
    context_object_name = 'products'
    paginate_by = 1
    count = 0

    def get_queryset(self):
        request = self.request
        query = request.GET.get('search_product')
        print(query)

        if query:
            qs = Product.objects.filter(title__contains=query).order_by('title')
            print(qs)
            self.count = len(qs)  # since qs is actually a list
            return qs

    def get_context_data(self, *args, **kwargs):
        try:
            context = super(SearchProduct, self).get_context_data()
            context['count'] = self.count or 0
            context['query'] = self.request.GET.get('search_product')
            return context
        except:
            pass