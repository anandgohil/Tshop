
from django.shortcuts import render

from store.models import Order


from django.views.generic.list import ListView





class OrderListView(ListView):
    template_name = 'store/order.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date').exclude(order_status='PENDING')