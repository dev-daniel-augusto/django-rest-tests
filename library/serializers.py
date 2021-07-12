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
        fields = ('author_name', 'created', 'modified')


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('language_name', 'created', 'modified')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_name', 'created', 'modified')


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('publisher_name', 'created', 'modified')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'book_name',
            'author',
            'category',
            'number_of_pages',
            'language',
            'publisher',
            'condition',
            'book_description',
        )


class RatingSerializer:

    class Meta:
        model = Rating
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'title',
            'customer',
            'review',
            'stars',
            'email',
        )
