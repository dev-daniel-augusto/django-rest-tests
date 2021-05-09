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
            'id',
            'title',
            'pages',
            'condition',
            'price',
            'category',
        )

    def validate_price(self, value):
        if value > 0:
            return value
        raise serializers.ValidationError(
            f" You've sent the value {value} to the price field. The price must be higher than 0")

    def validate_title(self, string):
        if string[0] == string.capitalize()[0]:
            return string
        raise serializers.ValidationError(
            f"You've sent the string {string} to the title field. The first letter must be upper case")

    def validate_pages(self, value):
        if value > 0:
            if value <= 50560:
                return value
        if value < 0:
            raise serializers.ValidationError(
                f"You've sent the value {value} to the pages field. The pages number must be higher than 0")
        raise serializers.ValidationError(
            f"You've sent the value {value} to the pages field. The max length allowed is 50560 pages")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
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
            'id'
            'title',
            'name',
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
