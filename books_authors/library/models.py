from django.db import models
from django.db.models import Avg
from mptt.models import MPTTModel, TreeForeignKey

from books_authors.users.models import User

REVIEW_RATES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Genre(MPTTModel):
    name = models.CharField(max_length=20, unique=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children'
                            )

    class MPTTMeta:
        order_insertion_by = ['name', ]

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books_by_author')
    annotation = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='books_by_genre')

    @property
    def rating(self):
        filtered_query = Rating.objects.filter(book=self)
        average_rating = filtered_query.aggregate(Avg('value')).get('value__avg')
        total_rates = filtered_query.count()
        return dict(average_rating=average_rating, amount_of_rates=total_rates)

    @property
    def reviews(self):
        output_reviews = []
        reviews = Review.objects.filter(book=self)
        for review in reviews:
            username = review.written_by.username
            text = review.text
            created_at = review.created_at

            try:
                rate = Rating.objects.get(user=review.written_by).value
            except Exception, e:
                rate = None

            output_reviews.append(dict(username=username, text=text, rate=rate, created_at=created_at))

        return output_reviews

    def __unicode__(self):
        return self.title


class Rating(models.Model):
    user = models.OneToOneField(User)
    book = models.ForeignKey(Book)
    value = models.PositiveIntegerField()

    def __unicode__(self):
        return '{0} rated {1} for {2}'.format(self.user, self.book, self.value)


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews_on_book')
    text = models.TextField(max_length=140)
    user = models.ForeignKey(User, related_name='reviews_by_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<{0}> by {1} on {2}'.format(self.book, self.written_by, self.created_at)
