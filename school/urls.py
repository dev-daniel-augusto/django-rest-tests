from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import (
                    ParentVewSet,
                    PhoneViewSet,
                    StudentViewSet,
                    )

router = SimpleRouter()
router.register('parents', ParentVewSet)
router.register('parents_phones', PhoneViewSet)
router.register('students', StudentViewSet)

