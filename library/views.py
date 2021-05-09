from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import (
                    Book,
                    Author,
                    Rating,
                    Category,
                    )
from .serializers import (
                    BookSerializer,
                    AuthorSerializer,
                    RatingSerializer,
                    CategorySerializer,
                    )


class BooksAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorsAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        if self.kwargs.get('book_pk'):
            return self.queryset.filter(id=self.kwargs.get('book_pk'))
        return self.queryset.all()


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        if self.kwargs.get('book_pk'):
            return get_object_or_404(self.get_queryset(),
                                     self.queryset.filter('book_pk'),
                                     pk=self.kwargs.get('ratings_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('ratings_pk'))


class CategoriesAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
