from rest_framework import serializers

from books_authors.library.models import Author, Book, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'books_by_genre',)
        read_only_fields = ('id',)
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name', 'books_by_author',)
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'annotation', 'genre',)
        read_only_fields = ('id',)
        depth = 1
