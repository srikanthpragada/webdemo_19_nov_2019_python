import django.forms as forms


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    mobile = forms.RegexField(regex=r"^\d{10}$", required=False)
