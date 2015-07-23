from django.views.generic import TemplateView

from .forms import AuthorForm


class AuthorsView(TemplateView):
    template_name = 'library/authors.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorsView, self).get_context_data(**kwargs)
        context.update(add_author_form=AuthorForm())
        print(context)

        return context
