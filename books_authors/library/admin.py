from django.contrib import admin

from .models import Author, Book, Genre, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'annotation', 'genre',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
