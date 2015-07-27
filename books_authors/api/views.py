from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import GenreSerializer, BookSerializer, BookAddSerializer, AuthorSerializer

from books_authors.library.models import Genre, Author, Book


def is_admin(request):
    if request.user.is_staff:
        return True
    return False


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
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

    def __call_super(self, request, *args, **kwargs):
        if is_admin(request):
            return super(BookViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        if is_admin(request):
            return super(BookViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if is_admin(request):
            return super(BookViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if is_admin(request):
            return super(BookViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if is_admin(request):
            return super(BookViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
