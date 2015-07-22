from django.conf.urls import url

from .views import AddAuthorView

urlpatterns = [
    url(r'add_author/$', AddAuthorView.as_view(), name='add_author'),
]
