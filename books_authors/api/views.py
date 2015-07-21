from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import GenreSerializer, BookSerializer, AuthorSerializer

from books_authors.library.models import Genre, Author, Book


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
