from rest_framework import serializers

from .models import TestUuid


class UuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUuid
        fields = "__all__"
