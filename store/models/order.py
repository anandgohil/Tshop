from django.contrib.auth.models import User
from django.db import models

from store.models import SizeVarient,Tshirt


class Order(models.Model):
    orderstatus=(
        ('PENDING','Pending'),
        ('PLACED','Placed'),
        ('CANCELED','Canceled'),
        ('COMPLITED','Complited'),
    )
    methods=(
        ('CASH_ON_DELIVERY','cash_On_Delivery'),
        ('ONLINE','Online'),
    )
    order_status = models.CharField(max_length=15, choices=orderstatus)
    payment_method = models.CharField(max_length=30, choices=methods)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(null=False)
    date = models.DateTimeField(null=False,auto_now_add=True)
    shipping_addres = models.CharField(max_length=200, null=False)
    contact = models.CharField(max_length=12,null=False)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    size = models.ForeignKey(SizeVarient, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    date = models.DateTimeField(null=False, auto_now_add=True)
