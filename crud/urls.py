from django.urls import path
from .views import (
                    ParentView, CreateParentView, UpdateParentView, DeleteParentView,
                    PhoneView, CreatePhoneView, UpdatePhoneView, DeletePhoneView,
                    StudentView, CreateStudentView, UpdateStudentView, DeleteStudentView,
                    SubjectListView, CreateSubjectView, UpdateSubjectView, DeleteSubjectView,
                    TeacherView, CreateTeacherView, UpdateTeacherView, DeleteTeacherView,
                    )

urlpatterns = [
    path('parents/', ParentView.as_view(), name='parents'),
    path('parents/add/', CreateParentView.as_view(), name='create_parent'),
    path('parents/update/<int:pk>', UpdateParentView.as_view(), name='update_parent'),
    path('parents/delete/<int:pk>', DeleteParentView.as_view(), name='delete_parent'),
    path('phones/', PhoneView.as_view(), name='phones'),
    path('phones/add/', CreatePhoneView.as_view(), name='create_phone'),
    path('phones/update/<int:pk>/', UpdatePhoneView.as_view(), name='update_phone'),
    path('phones/update/int:<pk>/', DeletePhoneView.as_view(), name='delete_phone'),
    path('students/', StudentView.as_view(), name='students'),
    path('students/add/', CreateStudentView.as_view(), name='create_student'),
    path('students/update/<int:pk>/', UpdateStudentView.as_view(), name='update_student'),
    path('students/delete/<int:pk>/', DeleteStudentView.as_view(), name='delete_student'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('subjects/add/', CreateSubjectView.as_view(), name='create_subject'),
    path('subjects/update/<int:pk>/', UpdateSubjectView.as_view(), name='update_subject'),
    path('subjects/delete/<int:pk>/', DeleteSubjectView.as_view(), name='delete_subject'),
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('teachers/add/', CreateTeacherView.as_view(), name='create_teacher'),
    path('teachers/update/<int:pk>/', UpdateTeacherView.as_view(), name='update_teacher'),
    path('teachers/delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete_teacher'),
]
