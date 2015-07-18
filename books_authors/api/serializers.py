from rest_framework import serializers

from library.models import Author, Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        field = ('id', 'name', 'parent', 'slug', )
