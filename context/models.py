from django.db import models



class Context(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성 일자")
