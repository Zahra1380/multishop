from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product
from .cart_module import Cart
from . import models
from django.http import HttpResponse
import requests
import json
from account.models import UserAddress


# Create your views here.
class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        trasportation = models.Transportation.objects.all()
        return render(request, 'cart/cart_detail.html', {'cart': cart, 'transport': trasportation})

    def post(self, request):
        trans = models.Transportation.objects.get(title=request.POST.get('transport'))
        print(trans)
        return redirect('Cart:create-order', trans.id)


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        color, size, quantity = self.request.POST.get('color', 'empty'), \
            self.request.POST.get('size', 'empty'), \
            self.request.POST.get('quantity')
        # print(color, size, quantity)
        cart = Cart(request)
        product.quantity -= int(quantity)
        product.save()
        cart.add(product, quantity, color, size)
        return redirect('Cart:cart-detail')


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('Cart:cart-detail')


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request, pk):
        trans = models.Transportation.objects.get(id=pk)
        cart = Cart(request)
        print(cart.total_price())
        order = models.Order.objects.create(user=request.user, tot_price=cart.total_price(), transport=trans)
        for item in cart:
            models.OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            size=item['size'],
                                            color=item['color'],
                                            quantity=item['quantity'],
                                            price=item['price'],
                                            total=float(item['price']) * int(item['quantity'])
                                            )
        cart.clear()
        return redirect('Cart:order-detail', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(models.Order, id=pk)
        tot = sum(item.quantity * item.price for item in order.item.all())
        return render(request, 'cart/order_detail.html', {'order': order, 'tot': tot})


class ApplyDiscountView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print('hi')
        order = get_object_or_404(models.Order, id=pk)
        code = request.POST.get('Discount').strip()
        discount_code = get_object_or_404(models.Discount, name=code)
        if discount_code.quantity == 0:
            return redirect('Cart:order-detail', order.id)
        discount_code.quantity -= 1
        discount_code.save()
        order.tot_price = order.tot_price - (order.tot_price * (discount_code.percentage / 100))
        order.save()
        print(order.tot_price)
        return redirect('Cart:order-detail', order.id)


# zarinpal -> payment

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # description

# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/cart/verify/'


class SendRequestView(View):
    def post(self, request, pk):
        order = get_object_or_404(models.Order, id=pk, user=request.user)
        address = get_object_or_404(UserAddress, id=request.POST.get('address'))
        order.address = f'{address.address} - {address.phone - address.email}'
        order.save()
        request.session['order_id'] = str(order.id)
        req_data = {
            "merchant_id": MERCHANT,
            "amount": order.tot_price,
            "callback_url": CallbackURL,
            "description": description,
            "metadata": {"mobile": request.user.phone_number, "email": request.user.email}
        }

        req_header = {"accept": "application/json",
                      "content-type": "application/json"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            return redirect(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return render(request, 'cart/error_payment_getway.html', {'error_code': e_code, 'error_massage': e_message})

class Error(TemplateView):
    template_name = 'cart/error_payment_getway.html'

class VerifyView(View):
    def get(self, request):
        message, name, date = '', '', ''
        t_status = request.GET.get('Status')
        order_id = request.session['order_id']
        order = models.Order.objects.get(id=int(order_id))
        t_authority = request.GET['Authority']

        if request.GET.get('status') == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.tot_price,
                "authority": t_authority
            }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:
                    order.is_paid = True
                    order.save()
                    message = 'Transaction success.'
                    name = 'RefID:'
                    data = req.json()['data']['ref_id']

                elif t_status == 101:
                    message = 'Transaction submitted:'
                    name = ''
                    data = req.json()['data']['message']
                else:
                    message = 'Transaction failed.'
                    name = 'Status:'
                    data = req.json()['data']['message']
                return render(request, '', {'message': message, 'name': name, 'data': data})

            else:

                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

        else:
            return HttpResponse('Transaction failed or canceled by user')


class BasketView(View):
    def get(self, request):
        order = models.Order.objects.filter(is_paid=False, user=request.user)
        return render(request, 'cart/basket.html', {'unpaid_order': order})