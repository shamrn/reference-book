from django import forms
from .models import ReferenceBookData


class UpdateBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['version'].widget.attrs['readonly'] = True  # отключаем изменение поля version

    class Meta:
        model = ReferenceBookData
        fields = ('name', 'short_name', 'desc', 'version', 'date')
