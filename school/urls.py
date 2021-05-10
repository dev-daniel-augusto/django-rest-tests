from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import (
                    ParentVewSet,
                    PhoneViewSet,
                    StudentViewSet,
                    ParentsAPIView,
                    PhonesAPIView,
                    StudentsAPIView,
                    ParentAPIView,
                    PhoneAPIView,
                    StudentAPIView,
                    SubjectAPIView,
                    TeacherAPIView,
                    SubjectsAPIView,
                    TeachersAPIView,
                    )

router = SimpleRouter()
router.register('parents', ParentVewSet)
router.register('parents-phones', PhoneViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('parents/', ParentsAPIView.as_view(), name='parents'),
    path('parents/<int:pk>/', ParentAPIView.as_view(), name='parent'),
    path('parents/<int:parent_pk>/students/', StudentsAPIView.as_view(), name='parent_students'),
    path('parents/<int:parent_pk>/students/<int:student_pk>/', StudentAPIView.as_view(), name='parent_student'),
    path('parents-phones/', PhonesAPIView.as_view(), name='phones'),
    path('parents-phones/<int:pk>/', PhoneAPIView.as_view(), name='phone'),
    path('students/', StudentsAPIView.as_view(), name='students'),
    path('students/<int:pk>/', StudentAPIView.as_view(), name='student'),
    path('subjects/', SubjectsAPIView.as_view(), name='subjects'),
    path('subjects/<int:pk>', SubjectAPIView.as_view(), name='subject'),
    path('subjects/<int:subject_pk>/teachers/', SubjectsAPIView.as_view(), name='subject_teachers'),
    path('subjects/<int:subject_pk>/teachers/<int:teacher_pk/', TeacherAPIView.as_view(), name='subject_teacher'),
    path('teachers/', TeachersAPIView.as_view(), name='teachers'),
    path('teachers/<int:pk>/', TeacherAPIView.as_view(), name='teacher')
]
