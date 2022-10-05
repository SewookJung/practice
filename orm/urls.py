from django.urls import path

from .views import PrefetchView

urlpatterns = [path("orm", PrefetchView.as_view(), name="prefect_related")]
