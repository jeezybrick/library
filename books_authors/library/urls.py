from django.conf.urls import url

from .views import AuthorsView

urlpatterns = [
    url(r'^$', AuthorsView.as_view(), name='authors'),
]
