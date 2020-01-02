from django.contrib import admin
from django.urls import path
from . import views, books_views

urlpatterns = [
    path("welcome/", views.welcome),
    path("greet/", views.greet),
    path("wish/", views.wish),
    path("discount/", views.calculate_discount),
    path("authors/", views.list_authors),
    path("addauthor/", views.add_author),
    path("updateauthor/", views.update_author),
    path("ajax/", views.ajax_demo),
    path("datetime/", views.ajax_datetime),
    path("books/home", books_views.book_home),
    path("books/list", books_views.book_list),
    path("books/add", books_views.book_add),
    path("books/delete/<int:id>", books_views.book_delete),
    path("books/edit/<int:id>", books_views.book_edit),
    path("books/search", books_views.book_search),
    path("books/dosearch", books_views.book_do_search),
]
