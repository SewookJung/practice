from rest_framework.routers import DefaultRouter

from .views import PersonViewset

router = DefaultRouter(trailing_slash=False)
router.register(r"modelviewset", PersonViewset, basename="modelviewset")

urlpatterns = router.urls
