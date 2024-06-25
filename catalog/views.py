from django.shortcuts import render
from django.views import generic
from . import models

def index(request):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_available_instances = models.BookInstance.objects.filter(status__exact='A').count()
    num_authors = models.Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available_instances': num_available_instances,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = models.Book
    paginate_by = 20

class BookDetailsView(generic.DetailView):
    model = models.Book

class AuthorListView(generic.ListView):
    model = models.Author
    paginate_by = 20

class AuthorDetailsView(generic.DetailView):
    model = models.Author
