from django.contrib.auth.models import User
from django.db import models
from store.models import Tshirt

class SizeVarient(models.Model):
    SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large'),
        ('XXL','Extra Extra Large'),
    )

    price = models.IntegerField(null=False)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES, max_length=10)

    def __str__(self):
        return f'{self.size}'
