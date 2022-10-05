from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=128, verbose_name="피자 이름")
    price = models.IntegerField(verbose_name="가격")


class Topping(models.Model):
    name = models.CharField(max_length=128, verbose_name="토핑 이름")
    pizza = models.ForeignKey(
        Pizza, on_delete=models.CASCADE, related_name="topping", verbose_name="피자"
    )
