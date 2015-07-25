from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import GenreSerializer, BookSerializer, BookAddSerializer, AuthorSerializer

from books_authors.library.models import Genre, Author, Book


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookAddSerializer

    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        pk = kwargs.get('pk') or None
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)

        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
