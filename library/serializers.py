from rest_framework import serializers

from .models import (
    Author,
    Language,
    Category,
    Publisher,
    Book,
    Rating,
)


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'author_name')


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'language_name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category_name')


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('id', 'publisher_name')


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, queryset=Author.objects.all(), slug_field='author_name')
    category = serializers.SlugRelatedField(many=True, queryset=Category.objects.all(), slug_field='category_name')
    language = serializers.SlugRelatedField(queryset=Language.objects.all(), slug_field='language_name')
    publisher = serializers.SlugRelatedField(queryset=Publisher.objects.all(), slug_field='publisher_name')

    class Meta:
        model = Book
        fields = ('id',
                  'author',
                  'isbn_10',
                  'isbn_13',
                  'category',
                  'language',
                  'book_name',
                  'condition',
                  'publisher',
                  'number_of_pages',
                  'book_description',
                  )


class RatingSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='book_name')

    class Meta:
        model = Rating
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'stars',
            'title',
            'email',
            'review',
            'customer_name',
        )
