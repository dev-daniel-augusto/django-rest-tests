from rest_framework import generics
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


class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class RatingAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
