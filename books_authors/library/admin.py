from django.contrib import admin

from .models import Author, Book, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('title',)
    readonly_fields = ('_rating',)
    list_display = ('_rating',)

    def _rating(self, obj):
        return obj.rating.get_rating()


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
