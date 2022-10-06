from django.urls import path

from .views import OrmWithDatabaseView

urlpatterns = [
    path("orm/database", OrmWithDatabaseView.as_view(), name="orm_with_database")
]
