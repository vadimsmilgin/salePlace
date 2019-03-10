from django.contrib.auth.decorators import login_required

from basket.models import *


def total_sum_basket(request):
    if request.user.is_authenticated:
        basket = BasketUser()
        sum = basket.total_sum(request.user)
    else:
        sum = 0
    return {'total_sum': sum}
