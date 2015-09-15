from django.contrib import admin

from .models import Author, Book, Genre, Review, Rating


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('author__name', 'title', )
    list_display = ('author', 'title', )
    fields = ('author', 'title', 'annotation', 'genre',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    search_fields = ('book__title', 'user__username', )
