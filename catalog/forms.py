import django.forms as forms
from . models import Book

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    mobile = forms.RegexField(regex=r"^\d{10}$", required=False)


class UpdateAuthorForm(forms.Form):
    id = forms.IntegerField()
    email = forms.EmailField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
