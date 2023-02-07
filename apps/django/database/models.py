from django.db import models


class TestUuid(models.Model):
    uuid = models.UUIDField(unique=True, verbose_name="uuid")
