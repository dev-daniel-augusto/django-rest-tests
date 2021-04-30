from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    category = models.CharField('Category', max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Book(models.Model):
    CONDITION_CHOICES = (
        ('New', 'Brand new'),
        ('Used', 'Old'),
    )
    title = models.CharField('Title', max_length=300)
    pages = models.IntegerField('Number of Pages')
    condition = models.CharField('Condition', max_length=4, choices=CONDITION_CHOICES)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Author(models.Model):
    title = models.OneToOneField(Book, on_delete=models.CASCADE)
    author = ArrayField(models.CharField('Author(s)', max_length=200), size=10)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.author}'


class Rating(models.Model):

    class Star(models.IntegerChoices):
        AMAZING = 5
        GOOD = 4
        FINE = 3
        BAD = 2
        HORRIBLE = 1

    name = models.CharField('Name', max_length=300)
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=200)
    comment = models.TextField('Comment', blank=True)
    stars = models.IntegerField('Stars', choices=Star.choices)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['email', 'title']

    def __str__(self):
        return f'{self.title}'
