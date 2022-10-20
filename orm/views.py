from django.db import connection
from django.db.models import Prefetch
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Pizza, Topping


class OrmWithDatabaseView(generics.GenericAPIView):
    """PrefetchView Evaluated

    Check queryset evaluated by orm

    Check Point:
        - Check database hit count
    """

    def get(self, request, *args, **kwargs):
        """
        Case 1.
        Check out database hit point by django orm

        Object total count
         - Pizza: 4
         - Topping: 6
        """

        # Evaluated
        pizza_search_by_get = Pizza.objects.get(id=1)
        # output: 1
        print(len(connection.queries))
        print(pizza_search_by_get)
        # output: 1
        print(len(connection.queries))

        # Not evaluated
        pizza_search_by_all = Pizza.objects.all()
        # output: 0
        print(len(connection.queries))
        # Evaluated
        print(pizza_search_by_all)
        # output: 1
        print(len(connection.queries))

        # Not evaluated
        pizza_search_by_filter = Pizza.objects.filter(id=1)
        # output: 0
        print(len(connection.queries))
        # Evaluated
        print(pizza_search_by_filter)
        # output: 1
        print(len(connection.queries))

        return Response(data=None, status=status.HTTP_200_OK)


class OrmPrefetchView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        """Case 1
        Not used prefetch of objects

        Object total count
         - Pizza: 4
         - Topping: 6
        """

        pizza = Pizza.objects.all()  # Not evaluated

        for item in pizza:  # Evaluated & output: 1
            print(item)
            toppings = item.topping.all()  # Not evaluated
            print(toppings)  # Evaluated

        print(len(connection.queries))

        """Case 2
        Used prefetch get filter
        """

        pizza_by_related = Pizza.objects.prefetch_related("topping").get(
            name="불고기 피자"
        )  # Evaluated
        print(len(connection.queries))  # Database hit count: 2

        toppings = pizza_by_related.topping.all()  # Not evaluated
        list(toppings)  # Force evaluated & Not evaludated
        print(len(connection.queries))  # Database hit count: 2

        """Case 3
        Used prefetch all filter
        """

        pizza_by_related = Pizza.objects.all().prefetch_related(
            "topping"
        )  # Not evaluated

        print(len(connection.queries))  # Database hit count: 0

        for item in pizza_by_related:  # Evaluated
            toppings = item.topping.all()
            for topping in toppings:
                print(topping)
            print("Evaluated", item)

        print(len(connection.queries))  # Database hit count: 2

        for item in pizza_by_related:  # Not evaluated
            print("Cached", item)

        for item in pizza_by_related:  # Not evaluated
            toppings = item.topping.all()

            for topping in toppings:  # Not evaluated
                print(topping)

        print(len(connection.queries))  # Database hit count: 2

        """Case 4
        Related model filtering with prefetch object
        """

        pizza_by_related = Pizza.objects.all().prefetch_related(
            Prefetch(
                "topping",
                queryset=Topping.objects.filter(name="올리브"),
                to_attr="olive_topping",
            )
        )

        for pizza in pizza_by_related:
            print(pizza, end=" ")
            olive_topping = pizza.olive_topping
            print(olive_topping)

        # """Case 5
        # Bad referance get related model
        # """

        pizza_by_related = Pizza.objects.prefetch_related(
            "topping"
        ).all()  # Not evaluated
        print(len(connection.queries))  # Database hit count: 0

        for item in pizza_by_related:  # Evaluated
            toppings = item.topping.filter(name="올리브")
            for topping in toppings:
                print(topping)

        return Response(data=None, status=status.HTTP_200_OK)
