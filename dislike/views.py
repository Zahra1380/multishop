from django.shortcuts import render, redirect
from django.views import View
from .models import DislikeModel
from like.models import LikeModel
from product.models import Product
from .sessions_module import Dislike


class AddDisLikeProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        dislike = Dislike(request)

        model_like = LikeModel.objects.filter(liker=request.user, product=product)
        model_dislike = DislikeModel.objects.filter(disliker=request.user, product=product)
        if model_like:
            model_like.delete()

        if model_dislike:
            dislike.delete(f'{request.user.id}-{product.slug}')
            model_dislike.delete()

        else:
            dislike.add(product, request.user)
            DislikeModel.objects.create(disliker=request.user, product=product)
            dislike.delete(f'{request.user.id}-{product.slug}')

        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('home:home')


class DisLike_list(View):
    def get(self, request):
        dislike = DislikeModel.objects.all().filter(disliker=request.user)
        return render(request, 'like/like_page.html', {'opinion': dislike})


class DisLikeDetail(View):
    def get(self, request, pk):
        dislike = DislikeModel.objects.get(id=pk)
        return render(request, 'like/like_detail.html', {'opinion': dislike})
