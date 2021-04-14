from django.test import TestCase
from .models import Book, Author
from .static_functions import update_authors, update_categories

class BooksModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        book = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", published_date="1997")
        book.average_ratings = 5
        book.ratings_count = 21
        book.save()

    def test_book_title(self):
        book = Book.objects.get(id=1)
        book_title = book.title
        self.assertEqual(book_title, "Harry Potter and the Sorcerer's Stone")

    def test_published_date(self):
        book = Book.objects.get(id=1)
        book_title = book.published_date
        self.assertEqual(book_title, "1997")

    def test_average_ratings(self):
        book = Book.objects.get(id=1)
        book_title = book.average_ratings
        self.assertEqual(book_title, 5)

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        book_title_max_length = book._meta.get_field('title').max_length
        self.assertEqual(book_title_max_length, 128)

    def test_book_str_view(self):
        book = Book.objects.get(id=1)
        book_str = f"Harry Potter and the Sorcerer's Stone"
        self.assertEqual(book_str, str(book))

    def test_add_author(self):
        book = Book.objects.get(id=1)
        authors = ['J.K. Rowling 2', 'J.K. Rowling 3']
        update_authors(book, authors)
        self.assertEqual(len(book.authors.all()), 2)
        authors = ''
        update_authors(book, authors)
        self.assertEqual(len(book.authors.all()), 0)

    def test_add_category(self):
        book = Book.objects.get(id=1)
        categories = ['Literary Criticism', 'Computers', 'Juvenile Fiction']
        update_categories(book, categories)
        self.assertEqual(len(book.categories.all()), 3)
        categories = ''
        update_categories(book, categories)
        self.assertEqual(len(book.categories.all()), 0)

class BooksViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        for book_id in range(10):
            book = Book.objects.create(title=f'Harry Potter part {book_id}',
                                published_date=str(int(1996+book_id)))
            authors = ['J.K. Rowling']
            update_authors(book, authors)

    def test_url_exists(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)

    def test_url_single(self):
        response = self.client.get('/api/books/1/')
        self.assertEqual(response.status_code, 200)

    def test_url_filter_published_date(self):
        response = self.client.get('/api/books/?published_date=1997')
        self.assertEqual(response.status_code, 200)

    def test_author_count(self):
        authors = Author.objects.all()
        self.assertEqual(len(authors), 1)

