from django.views.generic import TemplateView

from .forms import AuthorForm


class AddAuthorView(TemplateView):
    template_name = 'author_view.html'

    def get_context_data(self, **kwargs):
        context = super(AddAuthorView, self).get_context_data(**kwargs)
        context.update(add_author_form=AuthorForm)

        return context
