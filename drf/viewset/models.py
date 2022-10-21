from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128, verbose_name="이름")
    age = models.PositiveSmallIntegerField(verbose_name="나이")
    addr = models.CharField(max_length=128, verbose_name="주소")
    addr_detail = models.CharField(max_length=128, verbose_name="상세 주소")

    class Meta:
        db_table = "person"
