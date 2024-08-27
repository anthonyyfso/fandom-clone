from django import forms

from .models import Pages

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ('title', 'slug', 'text')

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if slug and Pages.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This slug is already taken.")
        return slug
        
