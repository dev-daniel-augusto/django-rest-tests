from rest_framework import filters
from rest_framework import generics
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Author,
    Language,
    Category,
    Publisher,
    Book,
    Rating,
)
from .filters import (
    AuthorFilter,
    LanguageFilter,
    CategoryFilter,
    PublisherFilter,
    BookFilter,
    RatingFilter,
)
from .throttles import (
    SustainedRateThrottle,
    AverageRateThrottle,
)
from .serializers import (
    AuthorSerializer,
    LanguageSerializer,
    CategorySerializer,
    PublisherSerializer,
    BookSerializer,
    RatingSerializer,
)


class BooksAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_class = BookFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['author__author_name', 'category__category_name', '=number_of_pages',
                     '=isbn_10', '=isbn_13', 'book_name', 'book_description',
                     'language__language_name', 'publisher__publisher_name',
                     'condition']
    ordering = ['id']
    ordering_fields = '__all__'
    throttle_classes = [SustainedRateThrottle]

    def get_queryset(self):
        if self.kwargs.get('language_pk'):
            return self.queryset.filter(language=self.kwargs.get('language_pk'))
        return self.queryset.all()


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [AverageRateThrottle]


class AuthorsAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['author_name']
    ordering = ['id']
    ordering_fields = '__all__'
    throttle_classes = [SustainedRateThrottle]

    def get_queryset(self):
        if self.kwargs.get('book_pk'):
            return self.queryset.filter(authors=self.kwargs.get('book_pk'))
        return self.queryset.all()


class AuthorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    throttle_classes = [AverageRateThrottle]


class LanguagesAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filterset_class = LanguageFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['language_name']
    ordering = ['id']
    ordering_fields = '__all__'
    throttle_classes = [SustainedRateThrottle]


class LanguageAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    throttle_classes = [AverageRateThrottle]


class CategoriesAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['category_name']
    ordering = ['id']
    ordering_fields = '__all__'
    throttle_classes = [SustainedRateThrottle]

    def get_queryset(self):
        if self.kwargs.get('book_pk'):
            return self.queryset.filter(categories=self.kwargs.get('book_pk'))
        return self.queryset.all()


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [AverageRateThrottle]


class PublishersAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filterset_class = PublisherFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['publisher_name']
    ordering = ['id']
    ordering_fields = '__all__'
    throttle_classes = [SustainedRateThrottle]


class PublisherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    throttle_classes = [AverageRateThrottle]


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filterset_class = RatingFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['email', 'customer_name', 'review', 'stars', 'title__book_name']
    ordering = ['id']
    ordering_fields = '__all__'
    throttle_classes = [SustainedRateThrottle]

    def get_queryset(self):
        if self.kwargs.get('book_pk'):
            return self.queryset.filter(title=self.kwargs.get('book_pk'))
        return self.queryset.all()


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    throttle_classes = [AverageRateThrottle]
