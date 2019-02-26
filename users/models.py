from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.FloatField(db_index=True, verbose_name="Текущий баланс", default=100.0)
    ava = models.ImageField(upload_to='users/', blank=True, verbose_name="")


