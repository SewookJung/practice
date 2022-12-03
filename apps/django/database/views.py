from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from .models import TestUuid
from .serializers import UuidSerializer


class TestUuidView(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = TestUuid.objects.all()
    serializer_class = UuidSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
