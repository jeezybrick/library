from django.conf.urls import url

from .views import AuthorsView, BooksView

urlpatterns = [
    url(r'^$', AuthorsView.as_view()),
    url(r'^authors/$', AuthorsView.as_view(), name='authors'),
    url(r'^books/$', BooksView.as_view(), name='books'),
]
