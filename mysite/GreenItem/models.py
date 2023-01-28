from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)

    def __str__(self):
        return str(self.money)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    brand = models.CharField(max_length=200, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    reg_date = models.DateTimeField('register date', default=timezone.now)
    pur_date = models.DateTimeField('purchase date', blank=True, null=True)

    def __str__(self):
        return self.name
