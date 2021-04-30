from django.contrib import admin
from .models import (
                    Book,
                    Author,
                    Rating,
                    Category,
                    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pages', 'condition',  'price', 'category']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'stars']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
