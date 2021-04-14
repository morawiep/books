from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import BookSerialzer, AuthorSerializer
from .models import Book, Author, Category
from django.views.decorators.csrf import csrf_exempt
from .web_scraping import scrape
from .static_functions import update_authors, update_categories

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerialzer
    queryset = Book.objects.all()

    def get_queryset(self):
        authors = self.request.query_params.getlist('author', None)
        published_date = self.request.query_params.getlist('published_date', None)
        sort_values = self.request.query_params.get('sort', None)
        if authors:
            try:
                authors_objects = Author.objects.filter(name__in=authors).values_list('id', flat=True)
                books = Book.objects.filter(authors__in=authors_objects)
            except:
                books = Book.objects.all()
        elif published_date:
            try:
                books = Book.objects.filter(published_date__in=published_date)
            except:
                books = Book.objects.all()
        elif sort_values:
            try:
                books = Book.objects.order_by(sort_values)
            except:
                books = Book.objects.all()
        else:
            books = Book.objects.all()
        return books

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BookSerialzer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        categories = request.POST.getlist('category')
        authors = request.POST.getlist('author')
        book = Book.objects.create(title=request.data['title'],
                                  published_date=request.data['published_date'])

        if request.POST.getlist('average_ratings'):
            book.average_ratings = request.data['average_ratings']
        if request.POST.getlist('ratings_count'):
            book.ratings_count = request.data['ratings_count']
        if request.POST.getlist('thumbnail'):
            book.thumbnail = request.data['thumbnail']
        if categories:
            update_categories(book, categories)
        if authors:
            update_categories(book, authors)
        book.save()
        serializer = BookSerialzer(book, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        book = self.get_object()
        categories = request.POST.getlist('category')
        authors = request.POST.getlist('author')
        if request.POST.getlist('title'):
            book.title = request.data['title']
        if request.POST.getlist('published_date'):
            book.published_date = request.data['published_date']
        if request.POST.getlist('average_ratings'):
            book.average_ratings = request.data['average_ratings']
        if request.POST.getlist('ratings_count'):
            book.ratings_count = request.data['ratings_count']
        if request.POST.getlist('thumbnail'):
            book.thumbnail = request.data['thumbnail']
        if categories:
            update_categories(book, categories)
        if authors:
            update_authors(book, authors)

        book.save()
        serializer = BookSerialzer(book, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return Response("Book deleted")

@csrf_exempt
def webscraping(request):
    if request.method == 'POST':
        filter_name = request.POST.getlist('q')
        filter_values = 'q=' + '&q='.join(filter_name)
        scrape_response = scrape(filter_values)
        return HttpResponse(scrape_response)
    return HttpResponse("Method is not correct")