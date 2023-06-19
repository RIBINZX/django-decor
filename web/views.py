from django.shortcuts import render
from . models import Book
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# Create your views here.
# def index(request):
#     books = Book.objects.all()
#     context = {
#         'hello': "enthan bro modayaano",
#         "book": books
#     }
#     return render(request, 'web/index.html', context

# def detail(request, slug):
#     book = Book.objects.get(slug=slug)
#     context = {
#         "book": book
#     }
#     return render(request, 'web/shopdatial.html', context)



class BookListView(ListView):
    model = Book
    template_name = "web/index.html"
    
    
class BookDetailView(DetailView):
    model = Book
    template_name = "web/shopdatial.html"
    
    
class BookCreateView(CreateView):
    model = Book
    template_name = "web/addbook.html"
    fields = '__all__'
    success_url = reverse_lazy('web:index')


    

