from django.urls import path

from .views import (
    AuthorsAPIView, AuthorAPIView,
    LanguagesAPIView, LanguageAPIView,
    CategoriesAPIView, CategoryAPIView,
    PublishersAPIView, PublisherAPIView,
    BooksAPIView, BookAPIView,
    RatingsAPIView, RatingAPIView,
)


urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='books_api'),
    path('books/<int:pk>/', BookAPIView.as_view(), name='book_api'),
    path('books/<int:book_pk>/ratings/', RatingsAPIView.as_view(), name='book_ratings_api'),
    path('books/<int:book_pk>/authors/', AuthorsAPIView.as_view(), name='book_authors_api'),
    path('books/<int:book_pk>/categories/', CategoriesAPIView.as_view(), name='book_categories_api'),

    path('authors/', AuthorsAPIView.as_view(), name='authors_api'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author_api'),

    path('languages/', LanguagesAPIView.as_view(), name='languages_api'),
    path('languages/<int:pk>/', LanguageAPIView.as_view(), name='language_api'),
    path('languages/<int:language_pk>/books/', BooksAPIView.as_view(), name='language_books_api'),

    path('categories/', CategoriesAPIView.as_view(), name='categories_api'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category_api'),

    path('publishers/', PublishersAPIView.as_view(), name='publishers_api'),
    path('publishers/<int:pk>/', PublisherAPIView.as_view(), name='publisher_api'),

    path('ratings/', RatingsAPIView.as_view(), name='ratings_api'),
    path('ratings/<int:pk>/', RatingAPIView.as_view(), name='rating_api')
]
