from django.db import models


class Core(models.Model):
    is_active = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Author(Core):
    author_name = models.CharField(max_length=250, unique=True)

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
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    number_of_pages = models.PositiveIntegerField()
    isbn_10 = models.PositiveBigIntegerField(unique=True)
    isbn_13 = models.PositiveBigIntegerField(unique=True)
    book_name = models.CharField(max_length=250, unique=True)
    book_description = models.TextField(blank=True, default='')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    condition = models.CharField(max_length=9, choices=CONDITION_CHOICES)

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

    email = models.EmailField(max_length=250)
    customer_name = models.CharField(max_length=300)
    review = models.TextField(blank=True, default='')
    stars = models.IntegerField('Stars', choices=Star.choices)
    title = models.ForeignKey(Book, related_name='ratings', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['email', 'title']

    def __str__(self):
        return f'{self.title}'
