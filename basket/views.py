from django.views.generic import ListView

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.decorators.http import require_POST

from basket.models import BasketUser
from shop.models import Item


@require_POST
def BasketAdd(request, item_id):
    item = Item.objects.get(id=item_id)
    user = User.objects.get(id=request.user.id)
    BasketUser().add(user, item)
    return redirect('basket:BasketDetail')

def BasketRemove(request, item_id):
    item = Item.objects.get(id=item_id)
    BasketUser().remove(item, request.user)
    return redirect('basket:BasketDetail')

def BasketPay(request):
    correct = BasketUser().pay(request.user)
    if correct:
        return render(request, 'paid.html')
    else:
        error = 'Проверте счет. Не хватает средств.'
        return render(request, 'paid.html', {'error': error})


class Basket(ListView):
    template_name = "basket.html"

    def get(self, request):
        basket = BasketUser.objects.filter(owner=request.user)
        total = BasketUser().total_sum(request.user)
        return render(request, 'basket.html', {'basket': basket, 'total': total})




