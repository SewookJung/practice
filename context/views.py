from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Context
from .serializers import (
    CustomContextSerializer,
    NotProvideContextSerializer,
    ProvideContextSerializer,
)

""" Context test

Purpose:
 - What is context?
 - How can use the context
 - Check provide default context
"""


class ProvideContextView(GenericAPIView):
    """ProvideContextView
    GenericAPIView
    get_serilaizer method include the get_serializer_context method
    get_serilaizer_context method is provide default contexts

    Check Point:
        - Inherited GenericAPIView
        - get_serializer
        - get_serializer_context

    Result:
        - context:{"request", "view", "format"}

    """

    queryset = Context.objects.all()
    serializer_class = ProvideContextSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)


class NotProvideContextView(GenericAPIView):
    """NotProvideContextView

    Even the GenericAPIView inherited, if use serializer directly does not provied
    default context

    Check Point:
        - Use serializer directly
        - Do not provide default context

    Result:
        - context:{}

    """

    queryset = Context.objects.all()
    serializer_class = NotProvideContextSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NotProvideContextSerializer(queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)


class CustomContextView(GenericAPIView):
    """CustomContextView

    Use custom context with default provide context

    Check Point:
        - Use provied context with custom context
        - Use only custom context

    Result:
        - context:{"request", "view", "format", "custom_context"}
        - context:{"custom_context"}

    """

    queryset = Context.objects.all()
    serializer_class = CustomContextSerializer

    def get_serializer_context(self):
        context = super(CustomContextView, self).get_serializer_context()
        print(context)
        context.update({"custom_context": "custom context data"})
        return context

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        custom_context_serializer = self.get_serializer(
            queryset, many=True, context={"custom_context": "data"}
        )
        print(custom_context_serializer.context)
        # result = {custom_context}

        update_default_provide_context = self.get_serializer(queryset, many=True)
        print(update_default_provide_context.context)
        # result = {request, format, view, custom_context}

        return Response(data=update_default_provide_context.data, status=HTTP_200_OK)
