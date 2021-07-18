from django.db import models


class Core(models.Model):
    is_active = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Author(Core):
    author_name = models.CharField(max_length=250 , unique=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.author_name


class Language(Core):
    language_name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.language_name


class Category(Core):
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Publisher(Core):
    publisher_name = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.publisher_name


class Book(Core):
    CONDITION_CHOICES = (
        ('Brand New', 'Brand New'),
        ('Old', 'Old'),
    )
    author = models.ManyToManyField(Author, related_name='authors')
    isbn_10 = models.PositiveBigIntegerField(unique=True)
    isbn_13 = models.PositiveBigIntegerField(unique=True)
    category = models.ManyToManyField(Category, related_name='categories')
    language = models.ForeignKey(Language, related_name='languages', on_delete=models.CASCADE)
    condition = models.CharField(max_length=9, choices=CONDITION_CHOICES)
    book_name = models.CharField(max_length=250, unique=True)
    publisher = models.ForeignKey(Publisher, related_name='publishers', on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField()
    book_description = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.book_name


class Rating(Core):

    class Star(models.IntegerChoices):
        AMAZING = 5
        GOOD = 4
        FINE = 3
        BAD = 2
        HORRIBLE = 1

    stars = models.IntegerField('Stars', choices=Star.choices)
    title = models.ForeignKey(Book, related_name='ratings', on_delete=models.CASCADE)
    email = models.EmailField(max_length=250)
    review = models.TextField(blank=True, default='')
    customer_name = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['email', 'title']

    def __str__(self):
        return f'{self.title}'
