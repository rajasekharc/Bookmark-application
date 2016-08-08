from django import forms
from .models import Website


class Bookmarkform(forms.ModelForm):

    class Meta:
        model = Website
        fields = ('website_address','description',)

