from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import GenreSerializer, BookSerializer, AuthorSerializer, UserSerializer
from .permissions import IsAuthenticatedReadOnly

from books_authors.library.models import Genre, Author, Book
from books_authors.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
