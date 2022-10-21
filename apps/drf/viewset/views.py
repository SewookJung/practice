from rest_framework.viewsets import ModelViewSet

from .models import Person
from .serializers import PersonSerializer


class PersonViewset(ModelViewSet):
    """Practice ModelViewSet


    Check Point:
        1. What is ModelViewSet
        2. How to use ModelViewSet
        3. Check default provide method

    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
