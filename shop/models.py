from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, blank=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
        pass

    def get_absolute_url(self):
        return reverse('shop_category', kwargs={'slug': self.slug})


class Item(models.Model):
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='shop/product_icons/', blank=True, verbose_name="")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назвение")
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.FloatField(db_index=True, blank=True, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
        pass

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
        pass
