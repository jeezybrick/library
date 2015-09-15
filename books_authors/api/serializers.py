from rest_framework import serializers

from books_authors.library.models import Author, Book, Genre, Review, Rating
from books_authors.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_login', 'is_staff')


class UserIDNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )


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


class GenreIdNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorIdNameSerializer()
    genre = GenreIdNameSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'annotation', 'genre', 'reviews', 'rating',)
        read_only_fields = ('id',)
        depth = 2


class BookIDTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', )


class ReviewSerializer(serializers.ModelSerializer):

    written_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ('book', 'written_by', 'text', )


class RatingSerializer(serializers.ModelSerializer):

    user = UserIDNameSerializer()
    book = BookIDTitleSerializer()

    class Meta:
        model = Rating
        fields = ('id', 'book', 'user', 'value', )
        depth = 1
