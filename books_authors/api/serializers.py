from django.shortcuts import get_object_or_404
from rest_framework import serializers

from books_authors.library.models import Author, Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()

    class Meta:
        model = Genre
        fields = ('name', 'parent',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'slug',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'annotation', 'genre', 'slug',)

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        genre = Genre.objects.create(**genre_data)
        Book.object.create(genre=genre, **validated_data)

        return Book

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre')
        book = instance.book
        genre = get_object_or_404(**genre_data)
        book.save()
        genre.save()
        instance.save()

        return instance
