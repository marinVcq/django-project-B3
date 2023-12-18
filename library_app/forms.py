# yourappname/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'abstract', 'publication_date', 'image_url']
