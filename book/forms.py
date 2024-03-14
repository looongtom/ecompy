from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','image' ,'author','price','description','categories']  # Add other fields as needed
