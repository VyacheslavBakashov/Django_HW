from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    catalog = Book.objects.all()
    for book in catalog:
        book.pub_date = book.pub_date.strftime('%Y-%m-%d')
    context = {'catalog': catalog}
    return render(request, template, context)


def show_book(request, pub_date):

    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    temp_dict = {}
    keys = ['name', 'author', 'pub_date']

    for book in books:
        book.pub_date = book.pub_date.strftime('%Y-%m-%d')
        values = [book.name, book.author, book.pub_date]
        temp_dict.setdefault(f'{book.pub_date}', []).append(dict(zip(keys, values)))

    dates = temp_dict.keys()

    if pub_date not in dates:
        return redirect('books')

    page = list(dates).index(pub_date) + 1
    pagi = Paginator(list(temp_dict.values()), 1)
    cur_date = pagi.get_page(page)
    next_date, prev_date = None, None

    if cur_date.has_next():
        next_page = cur_date.next_page_number()
        next_date = pagi.get_page(next_page)[0][0]['pub_date']

    if cur_date.has_previous():
        prev_page = cur_date.previous_page_number()
        prev_date = pagi.get_page(prev_page)[0][0]['pub_date']

    context = {'catalog': cur_date[0],
               'page': cur_date,
               'next_date': next_date,
               'prev_date': prev_date,
               }

    return render(request, template, context)


def index(request):
    return redirect('books')
