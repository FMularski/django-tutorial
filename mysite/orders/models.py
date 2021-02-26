from django.db import models
from string import ascii_uppercase, digits
from django.utils import timezone
from customers.models import Customer
import random

def generate_code():
    length = 8
    while True:
        code = ''.join(random.choices(ascii_uppercase + digits, k=length))
        if code not in Order.objects.values_list('code', flat=True):
            break
    return code

class Order(models.Model):
    code = models.CharField(default=generate_code, max_length=64, unique=True)
    date = models.DateTimeField(default=timezone.now, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'[{self.code}] {self.date} {self.customer}'