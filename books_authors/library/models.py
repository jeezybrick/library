from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Author(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name


class Genre(MPTTModel):
    name = models.CharField(max_length=20, unique=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children'
                            )
    slug = models.SlugField(unique=True)

    class MPTTMeta:
        order_insertion_by = ['name', ]

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books_by_author')
    annotation = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='books_by_genre')
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title
