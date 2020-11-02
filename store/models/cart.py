from django.contrib.auth.models import User
from django.db import models

from store.models import SizeVarient
from store.models.size import SizeVarient


class Cart(models.Model):
    sizevarient = models.ForeignKey(SizeVarient,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
