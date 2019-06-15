from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','publisher','tag1','tag2','tag3','status','link']


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

