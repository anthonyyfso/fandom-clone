from django import forms

from .models import Pages, Details

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ('title', 'text')

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('title', 'subtitle', 'text',)
