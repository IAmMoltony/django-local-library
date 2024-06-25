from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint
import uuid

class BookGenre(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Enter the name of a book genre'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-details', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message='Genre already exists'
            )
        ]

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(
        max_length=1500,
        help_text='Enter a brief description of the book'
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13-character ISBN of the book'
    )
    language = models.CharField(
        max_length=30,
        default='English',
        help_text='Enter the book\'s language'
    )

    genre = models.ManyToManyField(BookGenre, help_text='Select book genre')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-details', args=[str(self.id)])
    
    def display_genre(self):
        genres = self.genre.all()
        return ', '.join([str(genre) for genre in genres])

class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='A unique ID for this instance of the book'
    )
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('M', 'Maintenance'),
        ('O', 'On loan'),
        ('A', 'Available'),
        ('R', 'Reserved')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='M',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'[{self.id}] {self.book.title}'

    def get_display_status(self):
        return dict(self.LOAN_STATUS).get(self.status)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
