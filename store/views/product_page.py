
from django.shortcuts import render
from store.models import Tshirt
from math import floor
from django.views.generic.base import TemplateView

class ProductTemplateView(TemplateView):
    template_name = 'store/product_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('slug')
        request = self.request

        tshirt = Tshirt.objects.get(slug=slug)
        size = request.GET.get('size')

        if size == None:
            size = tshirt.sizevarient_set.all().order_by('price').first()
        else:
            size = tshirt.sizevarient_set.get(size=size)
        size_price = floor(size.price)

        sell_price = size_price - (size_price * (tshirt.discount / 100))
        sell_price = floor(sell_price)
        context = {'tshirt': tshirt, "price": size_price, 'sell_price': sell_price, "active_size": size}
        return context

