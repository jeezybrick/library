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

    rating = serializers.ReadOnlyField(source='rating.get_rating')

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'annotation', 'genre', 'rating',)
        read_only_fields = ('id',)
        depth = 1
