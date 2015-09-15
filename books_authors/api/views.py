from django.core.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import GenreSerializer, BookSerializer, AuthorSerializer, UserSerializer, ReviewSerializer, \
    RatingSerializer
from .permissions import IsAuthenticatedReadOnly

from books_authors.library.models import Genre, Author, Book, Review, Rating
from books_authors.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
            text = request.data.get('text', None)
            book = get_object_or_404(Book, id=request.data.get('book', None))
            user = get_object_or_404(User, id=request.user.pk)
            review = Review(text=text, book=book, written_by=user)

            try:
                review.full_clean()
                review.save()
                return Response(data=review, status=status.HTTP_201_CREATED)
            except Exception, e:
                return Response(data=dict(error=str(e)), status=status.HTTP_400_BAD_REQUEST)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
