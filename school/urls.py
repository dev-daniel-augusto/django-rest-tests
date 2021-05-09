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
                    )

router = SimpleRouter()
router.register('parents', ParentVewSet)
router.register('parents-phones', PhoneViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('parents/', ParentsAPIView.as_view(), name='parents'),
    path('parents-phones/', PhonesAPIView.as_view(), name='phones'),
    path('students/', StudentsAPIView.as_view(), name='students'),
    path('parents/<int:pk>/', ParentAPIView.as_view(), name='parent'),
    path('parents-phones/<int:pk>/', PhoneAPIView.as_view(), name='phone'),
    path('students/<int:pk>/', StudentAPIView.as_view(), name='student'),
]
