from django.urls import path

from .views import (
    AuthorsAPIView, AuthorAPIView,
    LanguagesAPIView, LanguageAPIView,
    BooksAPIView, BookAPIView,
)


urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='books_api'),
    path('books/<int:pk>/', BookAPIView.as_view(), name='book_api'),
    path('authors/', AuthorsAPIView.as_view(), name='authors_api'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author_api'),
    path('languages/', LanguagesAPIView.as_view(), name='languages_api'),
    path('languages/<int:pk>/', LanguageAPIView.as_view(), name='language_api'),
]
