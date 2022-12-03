from django.db import models


class TestUuid(models.Model):
    uuid = models.UUIDField(verbose_name="uuid")
