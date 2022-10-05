from rest_framework import generics, status
from rest_framework.response import Response


class PrefetchView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {}
        return Response(data=data, status=status.HTTP_200_OK)
