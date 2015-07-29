from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from books_authors.users.models import User


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Genre(MPTTModel):
    name = models.CharField(max_length=20, unique=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children'
                            )

    class MPTTMeta:
        order_insertion_by = ['name', ]

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books_by_author')
    annotation = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='books_by_genre')

    def __unicode__(self):
        return self.title


class Rate(models.Model):
    owner = models.ForeignKey(User)
    value = models.PositiveIntegerField()
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return '{0} rated {1} for {2}'.format(self.owner, self.book, self.value)


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews_on_book')
    text = models.TextField(max_length=140)
    written_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<{0}> by {1} on {2}.'.format(self.book, self.written_by, self.created_at)
