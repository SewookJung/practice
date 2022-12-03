from django.db import models


class TestUuid(models.Model):
    uuid = models.UUIDField(unique=True, editable=True, verbose_name="uuid")
