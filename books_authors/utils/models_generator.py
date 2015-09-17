import json
from random import choice, randint
import datetime

import django
from faker import Factory
from model_mommy import mommy

from books_authors.library.models import Author, Book, Genre, Review, Rating, User


class LibraryGenerator(object):
    """
    Provides a methods for generating Django
    models and writing them into DB
    """

    def __init__(self, locale='en_US'):
        django.setup()
        self.user_credentials = dict()
        self.books = list(Book.objects.all())
        self.authors = list(Author.objects.all())
        self.genres = list(Genre.objects.all())
        self.reviews = list(Review.objects.all())
        self.rating = list(Rating.objects.all())
        self.users = list(User.objects.all())
        self.fake = Factory.create(locale=locale)

    def get_random_name(self):
        return self.fake.name()

    def get_random_words(self, words_count=3):
        random_text = self.fake.text()
        random_title = ' '.join([choice(random_text.split(' ')).capitalize() for _ in range(words_count)])

        return random_title

    def get_random_text(self):
        return self.fake.text()

    def generate_users(self, number_of_users=10):
        for _ in range(number_of_users):
            try:
                username = self.get_random_words(words_count=1)
                password = ''.join(self.get_random_words(words_count=3).split(' '))
                email = '{0}@{1}.com'.format(self.get_random_words(words_count=1), self.get_random_words(words_count=1))
                user = mommy.make(User, username=username, email=email)
                user.set_password(password)
                user.save()
                self.users.append(user)
                self.user_credentials.update({username: password})
                print '{0} user successfully created.'.format(user.username)
            except Exception, e:
                print e

        with open('user_credentials.json', 'w') as f:
            f.write(json.dumps(self.user_credentials, indent=2, sort_keys=True))

    def generate_authors(self, number_of_authors=10):
        for _ in range(number_of_authors):
            try:
                author_name = self.get_random_name()
                author_model = mommy.make(Author, name=author_name)
                self.authors.append(author_model)
                print 'Successfully generated {0} author.'.format(author_model.name)
            except Exception, e:
                print e

    def generate_books(self, number_of_books=None):
        if not number_of_books:
            number_of_books = len(self.authors) * 15
        for _ in range(number_of_books):
            try:
                options = {
                    'title': self.get_random_words(words_count=randint(1, 5)),
                    'author': choice(self.authors),
                    'annotation': self.get_random_text(),
                    'genre': [choice(self.genres)]
                }
                book = mommy.make(Book, **options)
                print 'Successfully generated "{0}" book, author: {1}'.format(book.title, book.author.name)
            except Exception, e:
                print e

    def generate_genres(self, number_of_genres=10):
        for _ in range(number_of_genres):
            try:
                genre = mommy.make(Genre, name=self.get_random_words(words_count=1))
                self.genres.append(genre)
                print 'Successfully generated "{0}" genre.'.format(genre.name)
            except Exception, e:
                print e

    def generate_reviews_and_ratings(self):
        number_of_reviews = len(self.users) * len(self.books)
        for _ in range(number_of_reviews):
            options = {
                'book': choice(self.books),
                'text': self.get_random_text(),
                'user': choice(self.users)
            }
            try:
                review = mommy.make(Review, **options)
                rating = mommy.make(Rating, value=randint(1, 5), **options)
                print 'Successfully generated review for "{0} book with rating {1}, user: {2}.'.format(
                    review.book.title,
                    rating.value, review.user.username)
            except Exception, e:
                print e


if __name__ == '__main__':
    generator = LibraryGenerator()
    start_time = datetime.datetime.now()
    generator.generate_authors()
    generator.generate_genres()
    generator.generate_books()
    generator.generate_users()
    generator.generate_reviews_and_ratings()
    end_time = datetime.datetime.now()
    print 'Elapsed time: ', end_time - start_time
