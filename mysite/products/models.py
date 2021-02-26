from django.db import models
import lorem
from string import ascii_uppercase, digits
from random import choices
from customers.models import Order

def generate_code():
    length = 4

    while True:
        code = ''.join(choices(ascii_uppercase + digits, k=length))
        if code not in Product.objects.values_list('code', flat=True):
            break
    return code

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=4, null=False, unique=True, default=generate_code)
    desc = models.CharField(max_length=1024, null=False, default=lorem.sentence)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'[{self.code}] self.name'