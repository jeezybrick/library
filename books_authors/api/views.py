from rest_framework import viewsets

from .serializers import GenreSerializer, BookSerializer, AuthorSerializer
from .permissions import IsAuthenticatedReadOnly

from books_authors.library.models import Genre, Author, Book


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedReadOnly,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
