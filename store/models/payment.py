from django.contrib.auth.models import User
from django.db import models
from store.models import Order



class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, auto_now_add=True)
    Payment_status = models.CharField(max_length=15,default="FAILED")
    payment_id = models.CharField(max_length=60)
    payment_request_id = models.CharField(max_length=60,unique=True, null=False)
