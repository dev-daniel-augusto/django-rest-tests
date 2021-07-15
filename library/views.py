from rest_framework import generics

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
    filterset_class = BookFilter
    throttle_classes = [SustainedRateThrottle]


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [AverageRateThrottle]


class AuthorsAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter
    throttle_classes = [SustainedRateThrottle]


class AuthorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    throttle_classes = [AverageRateThrottle]


class LanguagesAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filterset_class = LanguageFilter
    throttle_classes = [SustainedRateThrottle]


class LanguageAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    throttle_classes = [AverageRateThrottle]


class CategoriesAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    throttle_classes = [SustainedRateThrottle]


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [AverageRateThrottle]


class PublishersAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filterset_class = PublisherFilter
    throttle_classes = [SustainedRateThrottle]


class PublisherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    throttle_classes = [AverageRateThrottle]


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filterset_class = RatingFilter
    throttle_classes = [SustainedRateThrottle]


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = PublisherSerializer
    throttle_classes = [AverageRateThrottle]
