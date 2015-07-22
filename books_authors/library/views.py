from django.views.generic import TemplateView

from .forms import AuthorForm


class AddAuthorView(TemplateView):
    template_name = 'add_author_form.html'

    def get_context_data(self, **kwargs):
        context = super(AddAuthorView, self).get_context_data(**kwargs)
        context.update(add_author_form=AuthorForm)

        return context
