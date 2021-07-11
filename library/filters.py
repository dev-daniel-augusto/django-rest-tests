import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains', label='Book Name:')
    book_name__istartswith = django_filters.CharFilter(field_name='book_name', lookup_expr='istartswith',
                                                       label='Book Name (Start with):')

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
