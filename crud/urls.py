from django.urls import path
from .views import (
                    IndexView,
                    CreateParentView,
                    UpdateParentView,
                    DeleteParentView,
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('parent/add/', CreateParentView.as_view(), name='create_parent'),
    path('parent/update/<int:pk>', UpdateParentView.as_view(), name='update_parent'),
    path('parent/delete/<int:pk>', DeleteParentView.as_view(), name='delete_parent')
]