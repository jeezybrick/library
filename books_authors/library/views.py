from django.views.generic import TemplateView


class AuthorsView(TemplateView):
    template_name = 'library/authors.html'


class BooksView(TemplateView):
    template_name = 'library/books.html'
