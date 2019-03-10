from threading import Thread

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404

from shop.models import Item
from users.models import Profile


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
            self = BasketUser.objects.filter(owner=user, item=item)
            self.delete()
        except BasketUser.DoesNotExist:
            pass

    def pay(self, user):
        totalSum = self.total_sum(user)
        profile = get_object_or_404(Profile, user=user)
        if totalSum > profile.account:
            return False
        else:
            for basket_item in BasketUser.objects.filter(owner=user):
                item_owner = basket_item.item.owner
                profile_owner = get_object_or_404(Profile, user=item_owner)
                profile_owner.account = profile_owner.account + basket_item.item.price
                profile.account = profile.account - basket_item.item.price
                profile_owner.save()
                profile.save()
                self.remove(basket_item.item, user)
                return True