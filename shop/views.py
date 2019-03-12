from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView
from shop.models import *
from django.shortcuts import render

from users.views import ProfileUser


class ProductList(ListView):
    template_name = "shop/items_list.html"
    model = Item
    #context_object_name = 'items'

    #def get_queryset(self, request):
    #    return Item.objects.exclude(owner=request.user)

    def get_context_data(self, **kwargs):
            context = super(ProductList, self).get_context_data(**kwargs)
            if self.request.user.is_authenticated:
                context['items'] = Item.objects.exclude(owner=self.request.user)
            else:
                context['items'] = Item.objects.all()
            return context


class SingleProduct(DetailView):
    template_name = "shop/item_details.html"

    def get(self, request, slug):
        item = get_object_or_404(Item, slug=slug)
        return render(request, self.template_name, {'item': item})


class SingleCategory(ListView):
    template_name = 'shop/cat_details.html'
    context_object_name = 'about_category'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Item.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(SingleCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
        pass


@require_POST
def deleteItem(request, item_id):
    profile = ProfileUser()
    item = get_object_or_404(Item, id=item_id)
    if item:
        item.delete()
    return profile.get(request, request.user.id)


