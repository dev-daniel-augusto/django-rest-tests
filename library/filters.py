import django_filters

from .models import (
    Author,
    Language,
    Category,
    Publisher,
    Book,
    Rating,
)


class AuthorFilter(django_filters.FilterSet):
    author_name = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    author_name__istarstwith = django_filters.CharFilter(field_name='author_name', lookup_expr='istartswith',
                                                         label='Author (Starts with):')
    author_name__iendswith = django_filters.CharFilter(field_name='author_name', lookup_expr='iendswith',
                                                       label='Author (Ends with):')

    class Meta:
        model = Author
        fields = ('author_name',)


class LanguageFilter(django_filters.FilterSet):
    language_name = django_filters.CharFilter(lookup_expr='icontains', label='Language')
    language_name__istarstwith = django_filters.CharFilter(field_name='language_name', lookup_expr='istartswith',
                                                           label='Language (Starts with):')
    language_name__iendswith = django_filters.CharFilter(field_name='language_name', lookup_expr='iendswith',
                                                         label='Language (Ends with):')

    class Meta:
        model = Language
        fields = ('language_name',)


class CategoryFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(lookup_expr='icontains', label='Category')
    category_name__istartswith = django_filters.CharFilter(field_name='category_name', lookup_expr='istartswith',
                                                           label='Category (Starts with):')
    category_name__iendswith = django_filters.CharFilter(field_name='category_name', lookup_expr='iendswith',
                                                         label='Category (Ends with):')

    class Meta:
        model = Category
        fields = ('category_name',)


class PublisherFilter(django_filters.FilterSet):
    publisher_name = django_filters.CharFilter(lookup_expr='icontains', label='Publisher')
    publisher_name__istartswith = django_filters.CharFilter(field_name='publisher_name', lookup_expr='istartswith',
                                                            label='Publisher (Starts with):')
    publisher_name__iendswith = django_filters.CharFilter(field_name='publisher_name', lookup_expr='iendswith',
                                                          label='Publisher (Ends with):')

    class Meta:
        model = Publisher
        fields = ('publisher_name',)


class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains', label='Book Name:')
    book_name__istartswith = django_filters.CharFilter(field_name='book_name', lookup_expr='istartswith',
                                                       label='Book Name (Starts with):')

    category__category_name = django_filters.CharFilter(lookup_expr='icontains', label='Category:')

    condition = django_filters.ChoiceFilter(choices=Book.CONDITION_CHOICES)

    number_of_pages = django_filters.NumberFilter(lookup_expr='exact', label='Number of Pages:')
    number_of_pages__gte = django_filters.NumberFilter(field_name='number_of_pages', lookup_expr='gte',
                                                       label='Number of Pages (Greater than or equal to):')
    number_of_pages__lte = django_filters.NumberFilter(field_name='number_of_pages', lookup_expr='lte',
                                                       label='Number of Pages (Less than or equal to):')

    publisher__publisher_name = django_filters.CharFilter(lookup_expr='icontains', label='Publisher:')

    language__language_name = django_filters.CharFilter(lookup_expr='icontains', label='Language:')

    class Meta:
        model = Book
        fields = ('book_name',)


class RatingFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(lookup_expr='icontains', label='Costumer')
    customer_name__istartswith = django_filters.CharFilter(field_name='customer_name', lookup_expr='istartswith',
                                                           label='Customer (Starts with):')
    customer_name__iendswith = django_filters.CharFilter(field_name='customer_name', lookup_expr='iendswith',
                                                         label='Customer (Ends with):')

    title__book_name = django_filters.CharFilter(lookup_expr='icontains', label='Book Name')
    title__book_name__istartswith = django_filters.CharFilter(field_name='title__book_name', lookup_expr='istartswith',
                                                              label='Book Name (Starts with):')
    title__book_name__iendswith = django_filters.CharFilter(field_name='title__book_name', lookup_expr='iendswith',
                                                            label='Book Name (Ends with):')

    review = django_filters.CharFilter(lookup_expr='icontains', label='Review (Search by keyword):')

    stars = django_filters.ChoiceFilter(choices=Rating.Star.choices)

    class Meta:
        model = Rating
        fields = ('customer_name',)
