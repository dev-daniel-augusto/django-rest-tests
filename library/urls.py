from django.urls import path
from .views import (
                    BooksAPIView,
                    BookAPIView,
                    AuthorsAPIView,
                    AuthorAPIView,
                    RatingsAPIView,
                    RatingAPIView,
                    CategoriesAPIView,
                    CategoryAPIView,
                    )

urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='books'),
    path('books/<int:pk>/', BookAPIView.as_view(), name='book'),
    path('authors/', AuthorsAPIView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author'),
    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('ratings/<int:pk>/', RatingAPIView.as_view(), name='rating'),
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name="category"),
]
