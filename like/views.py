from django.shortcuts import render, redirect
from django.views import View
from .models import LikeModel
from product.models import Product
from dislike.models import DislikeModel
from .sessions_module import Like
from product.models import Product

class AddLikeProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        like = Like(request)

        model_like = LikeModel.objects.filter(liker=request.user, product=product)
        model_dislike = DislikeModel.objects.filter(disliker=request.user, product=product)
        if model_dislike:
            model_dislike.delete()

        if model_like:
            like.delete(f'{request.user.id}-{product.slug}')
            model_like.delete()

        else:
            like.add(product, request.user)
            LikeModel.objects.create(liker=request.user, product=product)
            like.delete(f'{request.user.id}-{product.slug}')



        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('home:home')

class Like_list(View):
    def get(self, request):
        like = LikeModel.objects.all().filter(liker=request.user)
        return render(request, 'like/like_page.html', {'opinion':like})


class LikeDetail(View):
    def get(self, request, pk):
        like = LikeModel.objects.get(id=pk)
        return render(request, 'like/like_detail.html', {'opinion': like})