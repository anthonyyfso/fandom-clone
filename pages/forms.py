from django import forms

from .models import Pages, Details


class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ('title', 'text', 'image')

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('title', 'subtitle', 'text',)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        if 'title' in initial:
            self.base_fields['title'].initial = initial['title']
        super().__init__(*args, **kwargs)
