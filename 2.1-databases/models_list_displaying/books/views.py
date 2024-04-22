from django.shortcuts import render
from django.core.paginator import Paginator

from models_list_displaying.books.models import Book
from datetime import datetime

def books_view(request):
    template = 'books/books_list.html'
    context = {}
    # return render(request, template, context)
    book_obj = Book.objects.oreder_by('pub_date')
    books_lst = []
    for book in books_obj:
        books_lst.append({
            'book_name': book.name,
            'book_author': book.author,
            'book_pub_date': book.pub_date.strftime('%Y-%m-%d'),
        })
    context = {
        'book_list': books_lst,
        'prev_page': '',
        'next_page': '',
    }
    return render(request, template, context)

def pub_date_view(request, pub_date):
    template = 'books/books_list.html'
    book_obj = Book.objects.oreder_by('pub_date')
    books_lst = []
    context = {}
    for book in books_obj:
        books_lst.append({
            'book_name': book.name,
            'book_author': book.author,
            'book_pub_date': book.pub_date.strftime('%Y-%m-%d'),
        })
    prev_page = ''
    next_page = ''
    show_book = {}
    for book in book_lst:
        if book['book_pub_date'] == pub_date:
            show_book = {
                'book_name': book['book_name'],
                'book_author': book['ook_author'],
                'book_pub_date': book['book_pub_date'],
            }
        elif book['book_pub_date'] < pub_date:
            prev_page = book['book_pub_date']
        elif book['book_pub_date'] > pub_date and next_page == '':
            next_page = book['book_pub_date']
    context = {
        'book_list': [show_book],
        'prev_page': prev_page,
        'next_page': next_page,
    }
    return render(request, template, context)