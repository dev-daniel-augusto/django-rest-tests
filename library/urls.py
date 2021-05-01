from django.urls import path
from .views import (
                    BookAPIView,
                    AuthorAPIView,
                    RatingAPIView,
                    CategoryAPIView,
                    )

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='books'),
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('ratings/', RatingAPIView.as_view(), name='ratings'),
    path('categories/', CategoryAPIView.as_view(), name='categories')
]
