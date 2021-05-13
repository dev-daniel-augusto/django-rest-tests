from django.urls import path
from .views import (
                    ParentView,
                    CreateParentView,
                    UpdateParentView,
                    DeleteParentView,
                    PhoneView,
                    CreatePhoneView,
                    UpdatePhoneView,
                    DeletePhoneView,
                    StudentView,
                    CreateStudentView,
                    UpdateStudentView,
                    DeleteStudentView,
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
]

