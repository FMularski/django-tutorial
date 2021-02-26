from django.db import models
from django.utils import timezone
import string
import random

class Customer(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

def generate_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if code not in Order.objects.values_list('code', flat=True):
            break
    return code

class Order(models.Model):
    code = models.CharField(default=generate_code, max_length=64, unique=True)
    date = models.DateTimeField(default=timezone.now, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'[{self.code}] {self.date} {self.customer}'



