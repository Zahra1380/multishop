from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, TemplateView
from django.views import View
from .models import Product, Category, ProductColor, ProductSize, Comment
from product.templatetags.custom_tag import like_dislike


class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        like_dislike(product)
        return render(request, 'product/product_detail.html', {'product': product})

    def post(self, request, slug):
        product = Product.objects.get(slug=slug)
        like_dislike(product)
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        print(parent_id, body)
        if parent_id:
            Comment.objects.create(body=body, user=request.user, product=product, parent_id=int(parent_id))
        else:
            Comment.objects.create(body=body, user=request.user, product=product)
        return render(request, 'product/product_detail.html', {'product': product})


class NavPartialView(TemplateView):
    template_name = 'includes/topbar_nav_bar.html'

    def get_context_data(self, **kwargs):
        context = super(NavPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()

        return context


class CategoryItemView(ListView):
    template_name = 'product/category_item.html'
    paginate_by = 1
    context_object_name = 'procuct'

    def get_queryset(self):
        pk = self.request.GET.get('pk')
        cat = Category.objects.get(id=pk)
        product = Product.objects.filter(category=cat)
        print(product)
        return product


class ProductsList(ListView):
    template_name = 'product/all_product_page.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 1

    def get_queryset(self, **kwargs):
        queryset = Product.objects.all()
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        newqueryset = None
        if colors:
            if not newqueryset:
                newqueryset = queryset.filter(color__color__in=colors).distinct()
            else:
                newqueryset.union(queryset.filter(color__color__in=colors).distinct())

        if sizes:
            if not newqueryset:
                newqueryset = queryset.filter(size__title__in=sizes).distinct()
            else:
                newqueryset.union(queryset.filter(size__title__in=sizes).distinct())

        if min_price and max_price:
            if not newqueryset:
                newqueryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()
            else:
                newqueryset.union(queryset.filter(price__lte=max_price, price__gte=min_price).distinct())
        if newqueryset:
            queryset = newqueryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        return context


class SortByPrice(ListView):
    template_name = 'product/all_product_page.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('price')
    paginate_by = 1

    def get_queryset(self, **kwargs):
        queryset = self.queryset
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        newqueryset = None
        if colors:
            if not newqueryset:
                newqueryset = queryset.filter(color__color__in=colors).distinct()
            else:
                newqueryset.union(queryset.filter(color__color__in=colors).distinct())

        if sizes:
            if not newqueryset:
                newqueryset = queryset.filter(size__title__in=sizes).distinct()
            else:
                newqueryset.union(queryset.filter(size__title__in=sizes).distinct())

        if min_price and max_price:
            if not newqueryset:
                newqueryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()
            else:
                newqueryset.union(queryset.filter(price__lte=max_price, price__gte=min_price).distinct())
        if newqueryset:
            queryset = newqueryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SortByPrice, self).get_context_data()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        return context


class SortByCreateDate(ListView):
    template_name = 'product/all_product_page.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-create')
    paginate_by = 1

    def get_queryset(self, **kwargs):
        queryset = self.queryset
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        newqueryset = None
        if colors:
            if not newqueryset:
                newqueryset = queryset.filter(color__color__in=colors).distinct()
            else:
                newqueryset.union(queryset.filter(color__color__in=colors).distinct())

        if sizes:
            if not newqueryset:
                newqueryset = queryset.filter(size__title__in=sizes).distinct()
            else:
                newqueryset.union(queryset.filter(size__title__in=sizes).distinct())

        if min_price and max_price:
            if not newqueryset:
                newqueryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()
            else:
                newqueryset.union(queryset.filter(price__lte=max_price, price__gte=min_price).distinct())
        if newqueryset:
            queryset = newqueryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SortByCreateDate, self).get_context_data()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        return context


class ShowingTenItem(ListView):
    template_name = 'product/all_product_page.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:10]
    paginate_by = 1

    def get_queryset(self, **kwargs):
        queryset = self.queryset
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        newqueryset = None
        if colors:
            if not newqueryset:
                newqueryset = queryset.filter(color__color__in=colors).distinct()
            else:
                newqueryset.union(queryset.filter(color__color__in=colors).distinct())

        if sizes:
            if not newqueryset:
                newqueryset = queryset.filter(size__title__in=sizes).distinct()
            else:
                newqueryset.union(queryset.filter(size__title__in=sizes).distinct())

        if min_price and max_price:
            if not newqueryset:
                newqueryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()
            else:
                newqueryset.union(queryset.filter(price__lte=max_price, price__gte=min_price).distinct())
        if newqueryset:
            queryset = newqueryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowingTenItem, self).get_context_data()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        return context


class ShowingTwentyItem(ListView):
    template_name = 'product/all_product_page.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:20]
    paginate_by = 1

    def get_queryset(self, **kwargs):
        queryset = self.queryset
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        newqueryset = None
        if colors:
            if not newqueryset:
                newqueryset = queryset.filter(color__color__in=colors).distinct()
            else:
                newqueryset.union(queryset.filter(color__color__in=colors).distinct())

        if sizes:
            if not newqueryset:
                newqueryset = queryset.filter(size__title__in=sizes).distinct()
            else:
                newqueryset.union(queryset.filter(size__title__in=sizes).distinct())

        if min_price and max_price:
            if not newqueryset:
                newqueryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()
            else:
                newqueryset.union(queryset.filter(price__lte=max_price, price__gte=min_price).distinct())
        if newqueryset:
            queryset = newqueryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowingTwentyItem, self).get_context_data()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        return context


class ShowingThirtyItem(ListView):
    template_name = 'product/all_product_page.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:30]
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowingThirtyItem, self).get_context_data()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        return context


class ShareProduct(TemplateView):
    template_name = 'product/share_product.html'

    def get_queryset(self, **kwargs):
        queryset = self.queryset
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        newqueryset = None
        if colors:
            if not newqueryset:
                newqueryset = queryset.filter(color__color__in=colors).distinct()
            else:
                newqueryset.union(queryset.filter(color__color__in=colors).distinct())

        if sizes:
            if not newqueryset:
                newqueryset = queryset.filter(size__title__in=sizes).distinct()
            else:
                newqueryset.union(queryset.filter(size__title__in=sizes).distinct())

        if min_price and max_price:
            if not newqueryset:
                newqueryset = queryset.filter(price__lte=max_price, price__gte=min_price).distinct()
            else:
                newqueryset.union(queryset.filter(price__lte=max_price, price__gte=min_price).distinct())
        if newqueryset:
            queryset = newqueryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ShareProduct, self).get_context_data()
        product_id = self.request.GET.get('product')
        context['product'] = Product.objects.get(id=product_id)
        return context


class SpecialProductsList(ListView):
    template_name = 'product/special_product.html'
    context_object_name = 'products'
    pro = Product.objects.all().filter(is_special=True)
    queryset = pro
    paginate_by = 1


class WomenProductsList(ListView):
    template_name = 'product/special_product.html'
    context_object_name = 'products'
    queryset = Product.objects.all().filter(gender__gender='women')
    paginate_by = 1


class MenProductsList(ListView):
    template_name = 'product/special_product.html'
    context_object_name = 'products'
    queryset = Product.objects.all().filter(gender__gender='men')
    paginate_by = 1


class KidsProductsList(ListView):
    template_name = 'product/special_product.html'
    context_object_name = 'products'
    queryset = Product.objects.all().filter(gender__gender='kids')
    paginate_by = 1
