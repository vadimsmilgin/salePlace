from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from shop.models import *
#from cart.forms import CartAddProductForm
from django.shortcuts import render, redirect


class ProductList(ListView):
    template_name = "shop/items_list.html"
    model = Category
    #queryset = Item.objects.all()
    #context_object_name = 'items'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.all()
            context['items'] = Item.objects.all()
            return context
            pass


class SingleProduct(DetailView):
#    model = Item
    template_name = "shop/item_details.html"
#    context_object_name = 'item'
    #cart_product_form = CartAddProductForm()

    def get(self, request, slug):
        product = get_object_or_404(Item, slug=slug)
        return render(request, self.template_name, {'item': product, 'cart_product_form': self.cart_product_form})



class SingleCategory(ListView):
    template_name = 'shop/cat_details.html'
    context_object_name = 'about_category'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Item.objects.filter(category=self.category)
        pass

    def get_context_data(self, **kwargs):
        context = super(SingleCategory, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.category
        return context
        pass

