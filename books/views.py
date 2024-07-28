from django.shortcuts import render
from django.views import View
from books.models import Book
from django.http import Http404

def landing_page(request):
    return render(request, 'landing.html')


class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        data = {
            "books": books
        }
        print(data)
        return render(request, 'books/list.html', data)

class BookDetail(View):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            data = {
                "book": book
            }
            return render(request, 'books/detail.html', data)
        except Book.DoesNotExist:
            raise Http404("Bunaqa kitob yuq")