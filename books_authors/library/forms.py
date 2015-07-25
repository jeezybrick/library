from djangular.forms import NgModelForm, NgModelFormMixin

from .models import Author


class AuthorForm(NgModelFormMixin, NgModelForm):
    class Meta:
        model = Author
        fields = ('name', 'slug',)
