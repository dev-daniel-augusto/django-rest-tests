from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
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
    permission_classes = (permissions.DjangoModelPermissions, )

    @action(detail=True, methods=['get'])
    def phones(self, request, pk=None):
        parent = self.get_object()
        serializer = PhoneSerializer(parent.telephones.all(), many=True)
        return Response(serializer.data)


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def parents(self, request, pk=None):
        student = self.get_object()
        serializer = ParentSerializer(student.parent_name.all(), many=True)
        return Response(serializer.data)


class ParentsAPIView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class PhonesAPIView(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class StudentsAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
