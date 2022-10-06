from django.db import connection
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Pizza


class OrmWithDatabaseView(generics.GenericAPIView):
    """PrefetchView Prefect function

    Checkout database hit by orm

    Check Point:
        - Database hit point
    """

    def get(self, request, *args, **kwargs):
        """
        Case 1.
        Check out database hit point by django orm

        Object total count
         - Pizza: 2
         - Topping: 3
        """

        # Database hit
        pizza_by_get_func = Pizza.objects.get(id=1)
        # output: 1
        print(pizza_by_get_func)
        print(len(connection.queries))

        # No database hit
        pizza_by_all_func = Pizza.objects.all()
        # output: 0
        print(len(connection.queries))
        # Database hit
        print(pizza_by_all_func)
        # output: 1
        print(len(connection.queries))

        # No database hit
        pizza_by_filtering = Pizza.objects.filter(id=1)
        # output: 0
        print(len(connection.queries))
        # Database hit
        print(pizza_by_filtering)
        # output: 1
        print(len(connection.queries))

        return Response(data=None, status=status.HTTP_200_OK)
