from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime
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

    def since_register_date(self):
        now_date = localtime(timezone.now()).date()
        register_date = self.reg_date.date()
        since_days = (now_date - register_date).days
        return since_days
