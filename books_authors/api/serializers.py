from rest_framework import serializers

from books_authors.library.models import Author, Book, Genre, Review
from books_authors.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_login', 'is_staff')


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


class AuthorIdNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        depth = 1


class GenreIdNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorIdNameSerializer()
    genre = GenreIdNameSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'annotation', 'genre', 'reviews_on_book',)
        read_only_fields = ('id',)
        depth = 2
