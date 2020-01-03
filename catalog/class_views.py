from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Book


class AboutView(TemplateView):
    template_name = "about.html"


class BooksList(ListView):
    model = Book

