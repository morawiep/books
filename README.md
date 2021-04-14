# Books REST API

#### List of books
https://books-stx.herokuapp.com/api/books/

#### List of authors
https://books-stx.herokuapp.com/api/authors/


#### Adding new books

##### POST request with parameters

###### Required parameters:
- title
- published_date

###### Not required parameters:
- authors
- categories
- average_ratings
- ratings_count
- thumbnail

https://books-stx.herokuapp.com/api/books/ 

#### Scraping books from website https://www.googleapis.com/books/v1/volumes?q=

POST request with parameter q

https://books-stx.herokuapp.com/db/

#### Update, delete and details book
###### PUT, DELETE, GET request
https://books-stx.herokuapp.com/api/books/<\id>

#### Search by author
https://books-stx.herokuapp.com/api/books/?author=Peter%20Turchin&author=Devin%20Brown

#### Search by published date
https://books-stx.herokuapp.com/api/books/?published_date=2012

#### Sort by published date
https://books-stx.herokuapp.com/api/books/?sort=published_date
