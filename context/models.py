from django.db import models


class Context(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성 일자")

    def get_id(self):
        return f"Name {self.name}"


class Test(models.Model):
    context = models.ForeignKey(
        Context, on_delete=models.CASCADE, verbose_name="context", related_name="test"
    )
