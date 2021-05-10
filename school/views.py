from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from .models import (
                    Parent,
                    Phone,
                    Student,
                    Subject,
                    Teacher,
                    )
from .serializers import (
                          ParentSerializer,
                          PhoneSerializer,
                          StudentSerializer,
                          SubjectSerializer,
                          TeacherSerializer,
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

    def get_queryset(self):
        if self.kwargs.get('parent_pk'):
            return self.queryset.filter(id=self.kwargs.get('parent_pk'))
        return self.queryset.all()


class StudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        if self.kwargs.get('parent_pk'):
            return get_object_or_404(self.get_queryset(),
                                     id=self.kwargs.get('parent_pk'),
                                     pk=self.kwargs.get('student_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('student_pk'))


class SubjectsAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        if self.kwargs.get('subject_pk'):
            return self.queryset.filter(id=self.kwargs.get('subject_pk'))
        return self.queryset.all()


class SubjectAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeachersAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
