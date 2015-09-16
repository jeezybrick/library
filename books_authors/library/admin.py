from django.contrib import admin

from .models import Author, Book, Genre, Review, Rating


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('author__name', 'title', )
    list_display = ('author', 'title', )
    fields = ('author', 'title', 'annotation', 'genre',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'text')
    search_fields = ('book', 'user', 'text')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'value')
    search_fields = ('book__title', 'user__username', )
