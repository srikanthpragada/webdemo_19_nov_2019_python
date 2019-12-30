from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import sqlite3
from .forms import AuthorForm, UpdateAuthorForm


def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome To Catalog Application!</h1>")


def greet(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    hours = datetime.now().hour
    if hours < 12:
        msg = "Good Morning"
    elif hours < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{msg} {name}</h1>")


def wish(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    hours = datetime.now().hour
    if hours < 12:
        msg = "Good Morning"
    elif hours < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return render(request, 'wish.html',
                  {'msg': msg, 'user': name})


def calculate_discount(request):
    if 'amount' in request.POST:  # request with data, so process it
        amount = float(request.POST['amount'])
        rate = float(request.POST['rate'])
        discount = amount * rate / 100
        return render(request, 'discount.html',
                      {'discount': discount, 'amount': amount, 'rate': rate})
    else:  # request without parameters(data)
        return render(request, 'discount.html')


def list_authors(request):
    con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
    cur = con.cursor()
    cur.execute("select * from authors")
    authors = cur.fetchall()
    con.close()
    return render(request, 'list_authors.html', {'authors': authors})


def add_author(request):
    if request.method == "GET":
        authorform = AuthorForm()
        return render(request, 'add_author2.html',
                      {'form': authorform})
    else:  # POST
        f = AuthorForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            mobile = f.cleaned_data['mobile']

            con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
            cur = con.cursor()
            try:
                cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)",
                        (name, email, mobile))
                con.commit()
            except Exception as ex:
                msg = "Sorry! Error : " + str(ex)
                return render(request, 'add_author2.html',
                              {'form': f, 'message' : msg})
            finally:
                con.close()

            return redirect("/catalog/authors")
        else:
            return render(request, 'add_author2.html', {'form': f})



def update_author(request):
    if request.method == "GET":
        form = UpdateAuthorForm()
        return render(request, 'update_author.html',
                      {'form': form})
    else:  # POST
        f = UpdateAuthorForm(request.POST)
        if f.is_valid():
            id = f.cleaned_data['id']
            email = f.cleaned_data['email']

            con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
            cur = con.cursor()
            try:
                cur.execute("update authors set email = ? where id = ?",
                        (email,id))
                if cur.rowcount == 1:
                   con.commit()
                   msg = "Updated Email Successfully!"
                else:
                   msg = "Sorry! Author id not found!"
            except Exception as ex:
                msg = "Sorry! Error : " + str(ex)
            finally:
                con.close()
                return render(request, 'update_author.html',
                              {'form': f, 'message': msg})
        else:
            return render(request, 'update_author.html',
                          {'form': f})

