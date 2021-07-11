from django.contrib import admin

from .models import (
    Author,
    Language,
    Category,
    Publisher,
    Book,
    Rating,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'created', 'modified', 'is_active')


@admin.register(Language)
class LanguegeAdmin(admin.ModelAdmin):
    list_display = ('language_name', 'created', 'modified', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created', 'modified', 'is_active')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('publisher_name', 'created', 'modified', 'is_active')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'book_name',
        'language',
        'publisher',
        'condition',
        'number_of_pages',
        'get_categories',
        'get_authors',
    )

    def get_categories(self, obj):
        return ', '.join([c.category_name for c in obj.category.all()])

    def get_authors(self, obj):
        return ', '.join([a.author_name for a in obj.author.all()])

    get_categories.short_description = 'Categories'

    get_authors.short_description = 'Authors'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('title', 'stars', 'created', 'modified', 'is_active')
