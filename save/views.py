from django.shortcuts import render, redirect
from django.views import View
from save.models import SaveModel
from product.models import Product
from .sessions_module import Save

class AddSaveProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        save = Save(request)

        model_save = SaveModel.objects.filter(saver=request.user, product=product)

        if model_save:
            save.delete(f'{request.user.id}-{product.slug}')
            model_save.delete()

        else:
            save.add(product, request.user)
            SaveModel.objects.create(saver=request.user, product=product)
            save.delete(f'{request.user.id}-{product.slug}')

        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('home:home')


class Save_list(View):
    def get(self, request):
        save = SaveModel.objects.all().filter(saver=request.user)
        return render(request, 'like/like_page.html', {'opinion': save})


class SaveDetail(View):
    def get(self, request, pk):
        save = SaveModel.objects.get(id=pk)
        return render(request, 'like/like_detail.html', {'opinion': save})
