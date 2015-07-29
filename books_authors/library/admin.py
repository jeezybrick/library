from django.contrib import admin

from .models import Author, Book, Genre, Review, Rate


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'annotation', 'genre',)
    readonly_fields = ('_rating',)
    list_display = ('_rating',)

    def _rating(self, obj):
        return obj.rating.get_rating()


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass
