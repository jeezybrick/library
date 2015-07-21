from rest_framework import serializers

from books_authors.library.models import Author, Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field='slug')

    class Meta:
        model = Genre
        fields = ('id', 'name', 'parent', 'slug',)
        read_only_fields = ('id',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'slug',)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), many=True, slug_field='slug')

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'annotation', 'genre', 'slug',)

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        genre = Genre.objects.create(**genre_data)
        Book.object.create(genre=genre, **validated_data)

        return Book
