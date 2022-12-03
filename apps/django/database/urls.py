from django.urls import path

from .views import TestUuidView

urlpatterns = [path("uuid", TestUuidView.as_view())]
