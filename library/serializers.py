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

    def create(self, validated_data):
        book = Book.objects.create(
            isbn_10=validated_data['isbn_10'],
            isbn_13=validated_data['isbn_13'],
            language=validated_data['language'],
            book_name=validated_data['book_name'],
            condition=validated_data['condition'],
            publisher=validated_data['publisher'],
            number_of_pages=validated_data['number_of_pages'],
        )
        book.author.set(validated_data['author'])
        book.category.set(validated_data['category'])
        return book

    def validate_isbn_13(self, isbn_13):
        isbn_13 = str(isbn_13)
        if len(isbn_13) != 13:
            raise serializers.ValidationError('Ensure this ISBN-13 digits are equal to 13')
        elif ''.join([isbn_13[0], isbn_13[1], isbn_13[2]]) == '978':
            return int(isbn_13)
        raise serializers.ValidationError('The first three digits of ISBN-13 must be 978')


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
