import requests
from .models import Book, Author, Category
from .static_functions import update_authors, update_categories

def scrape(url_filter):
    r = requests.get('https://www.googleapis.com/books/v1/volumes?' + url_filter)
    if r.status_code != 200:
        return "Request not correct"
    response_text = r.json()
    for item in response_text['items']:
        try:
            title = item['volumeInfo']['title']
            published_date = item['volumeInfo']['publishedDate']
            book, created = Book.objects.update_or_create(title=title, published_date=published_date)
            try:
                book.average_ratings = item['volumeInfo']['averageRating']
            except:
                book.average_ratings = ''
            try:
                book.ratings_count = item['volumeInfo']['ratingsCount']
            except:
                book.ratings_count = ''
            try:
                book.thumbnail = item['volumeInfo']['imageLinks']['thumbnail']
            except:
                book.thumbnail = ''
            try:
                authors = item['volumeInfo']['authors']
            except:
                authors = ''

            update_authors(book, authors)
            try:
                categories = item['volumeInfo']['categories']
            except:
                categories = ''
            update_categories(book, categories)

            book.save()
        except:
            return "Something went wrong during scraping data"
    return "Values scraped sucesfully"