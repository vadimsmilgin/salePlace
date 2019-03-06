from threading import Thread

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404

from shop.models import Item


class BasketUser(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def total_sum(self, user):
        total = 0
        for basket_item in BasketUser.objects.filter(owner=user):
            total += basket_item.item.price
        return total

    def add(self, user, item):
        item1 = Item.objects.get(id=item.id)
        try:
            new_item = BasketUser.objects.get(item=item1)
            if new_item not in BasketUser.objects.all():
                self.owner = user
                self.item = item
                self.save()
        except BasketUser.DoesNotExist:
            self.owner = user
            self.item = item
            self.save()

    def remove(self, item, user):
        item = Item.objects.get(id=item.id)
        try:
            del_item = BasketUser.objects.filter(owner=user, item=item)
            del_item.delete()
        except BasketUser.DoesNotExist:
            pass
       # for basket_item in BasketUser.objects.filter(owner=user, item=item):
       #     if basket_item.item == item:
        #        basket_item.delete()
       #         self.save()
