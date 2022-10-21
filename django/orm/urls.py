from django.urls import path

from .views import OrmPrefetchView, OrmWithDatabaseView

urlpatterns = [
    path("orm/database", OrmWithDatabaseView.as_view(), name="orm_with_database"),
    path("orm/prefetch", OrmPrefetchView.as_view(), name="orm_prefetch"),
]
