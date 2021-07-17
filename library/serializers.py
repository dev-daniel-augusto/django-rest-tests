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
    author = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(many=True, read_only=True)
    language = serializers.StringRelatedField(read_only=True)
    publisher = serializers.StringRelatedField(read_only=True)

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
    title = serializers.StringRelatedField(read_only=True)

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
