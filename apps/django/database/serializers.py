from rest_framework import serializers

from .models import TestUuid


class UuidSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(help_text="uuid")

    class Meta:
        model = TestUuid
        fields = "__all__"
        extra_kwargs = {"uuid": {"write_only": True}}
