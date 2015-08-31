import sys
from os import path, environ

sys.path.append(path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__))))))
environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.local'
from config.settings.local import DEBUG
from books_authors.library.models import Author, Book, Genre
