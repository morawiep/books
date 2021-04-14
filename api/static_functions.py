from .models import Author, Category


def update_authors(book, authors):
    for author_remove in book.authors.all():
        book.authors.remove(author_remove)
    for author in authors:
        current_author, created = Author.objects.get_or_create(name=author)
        book.authors.add(current_author)
    book.save()


def update_categories(book, categories):
    for category_remove in book.categories.all():
        book.categories.remove(category_remove)
    for category in categories:
        current_category, created = Category.objects.get_or_create(name=category)
        book.categories.add(current_category)
    book.save()
