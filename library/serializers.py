from rest_framework import serializers
from .models import (
                    Book,
                    Author,
                    Rating,
                    Category,
                    )


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title',
            'pages',
            'condition',
            'price',
            'category',
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'title',
            'author',
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = (
            'name',
            'title',
            'email',
            'comment',
            'stars',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'category',
        )
