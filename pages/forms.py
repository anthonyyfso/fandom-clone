from django import forms

from .models import Pages, Details, CharacterInformation


from django.forms import FileInput


class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ('title', 'text', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter title'}),
            'text': forms.Textarea(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter character information'}),
            'image': FileInput(attrs={'class': "formcontainer__slot--label"}),  # Use FileInput to hide current image
        }


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('title', 'subtitle', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter title'}),
            'subtitle': forms.TextInput(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter character information'}),  # Updated field name
            'text': forms.Textarea(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter detailed information', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        if 'title' in initial:
            self.base_fields['title'].initial = initial['title']
        super().__init__(*args, **kwargs)

class CharacterInformationForm(forms.ModelForm):
    class Meta:
        model = CharacterInformation
        fields = ('title', 'character_information', 'text',)  # Change 'subtitle' to 'character_information'
        widgets = {
            'title': forms.TextInput(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter title'}),
            'character_information': forms.TextInput(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter character information'}),  # Updated field name
            'text': forms.Textarea(attrs={'class': "formcontainer__slot--label", 'placeholder': 'Enter detailed information', 'rows': 5}),
        }



    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        if 'title' in initial:
            self.base_fields['title'].initial = initial['title']
        super().__init__(*args, **kwargs)