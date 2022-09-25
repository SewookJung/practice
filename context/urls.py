from django.urls import path

from .views import ProvideContextView, NotProvideContextView, CustomContextView


urlpatterns = [
    path("context/provide", ProvideContextView.as_view(), name="provide_context"),
    path("context/not/provide", NotProvideContextView.as_view(), name="not_provide_context"),
    path("context/custom", CustomContextView.as_view(), name="custom_context"),
]
