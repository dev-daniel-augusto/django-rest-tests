from rest_framework import viewsets
from .models import (
                    Parent,
                    Phone,
                    Student,
                    )
from .serializers import (
                        ParentSerializer,
                        PhoneSerializer,
                        StudentSerializer,
                         )


class ParentVewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
