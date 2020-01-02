from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .models import Book
from django.core.exceptions import ObjectDoesNotExist
from .forms import BookForm


def book_home(request):
    summary = Book.objects.all().aggregate(count=Count('id'), avgprice=Avg('price'))
    return render(request, 'books/home.html',
                  {'summary': summary})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html',
                  {'books': books})


def book_delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("/catalog/books/list")
    except ObjectDoesNotExist:
        return render(request, 'books/delete.html',
                      {'msg': 'Book Id Not Found!'})
    except:
        return render(request, 'books/delete.html',
                      {'msg': 'Book could not be deleted!'})


def book_add(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'books/add.html',
                      {'form': form})
    else:  # POST
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Add book to table
            return redirect("/catalog/books/list")
        else:
            return render(request, 'books/add.html',
                          {'form': form})


def book_edit(request, id):
    if request.method == "GET":
        try:
            book = Book.objects.get(id=id)
            form = BookForm(instance=book)
            return render(request, 'books/edit.html',
                          {'form': form})
        except ObjectDoesNotExist:
            return render(request, 'books/edit.html',
                          {'msg': 'Book Id Not Found!'})
    else: # POST
        book = Book.objects.get(id=id)
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()   # Update
            return redirect("/catalog/books/list")
        else:
            return render(request, 'books/edit.html',
                          {'form': form})



def book_search(request):
    return render(request, 'books/search.html')


def book_do_search(request):
    title = request.GET['title']
    # convert Book objects to dict
    books = list(Book.objects.filter(title__contains=title).values())
    # send list of dict in the form of array of json objects
    return JsonResponse(books, safe=False)
