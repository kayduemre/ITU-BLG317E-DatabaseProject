from flask.views import View
from flask import render_template, request, url_for, session, redirect
from services.database import Database
from repository.singUpRepository import createUser, findUser
from repository.LibraryRepository import createCategory, getCategorys
from repository.BookRepository import createAuthor, createBook, createPublisher, getBookById, update_Book

from models.data.entitiys.UserEntity import UserEntity
from models.data.entitiys.CategoryEntity import CategoryEntity
from models.data.entitiys.Book import Book
from models.data.entitiys.Author import Author
from models.data.entitiys.Publisher import Publisher
import hashlib
from datetime import datetime

class BookView(View):

    

    def dispatch_request(self, **kwargs):

        if kwargs.get('comment_id'):
            return render_template('./home.html')
        if request.method == 'POST':
            title = request.form.get('title')
            author = request.form.get('author')
            publisher = request.form.get('publisher')
            language = request.form.get('language')
            publish_date = request.form.get('publish_date')
            page_number = request.form.get('page_number')
            select = request.form.get('select')
            price = request.form.get('price')
            description = request.form.get('description')
            created_date = request.form.get('created_date')

            category_id = request.form.get('category')

            error = "Success"
            author = Author(author)
            authorId= createAuthor(author)
            publisher = Publisher(publisher,publish_date)
            publisher_id = createPublisher(publisher)

            if(authorId == 0 or publisher_id == 0):
                error = "Bilinmeyen hata"
                return render_template("/addBook.html")
            book = Book(title,authorId, description,publisher_id,language,page_number,price,created_date,session['user'][1], category_id)

        
   
            createBook(book)
            
        
        categorys = getCategorys(session['user'][1])
        context = categorys

        return render_template("/addBook.html", context = context)

def updateBook(**kwargs):
    book_id= kwargs.get('book_id')

    response = getBookById(book_id)

    res = {
        "title": response[0][2],
        'author': response[0][3],
        'summ' : response[0][4],
        'pub' : response[0][5],
        'pageNumber': response[0][7],
        'price': response[0][10],
        'language': response[0][9]
    }

    print(response[0][0])
    if request.method == 'POST':
        if 'form-title' in request.form:
            title = request.form.get('title')
            title_dic = {
                "title": title
            }
            update_Book(title_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))

            
        if 'form-author' in request.form:
            author = request.form.get('author')
            author_dic = {
                "author": author
            }
            update_Book(author_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))

        if 'form-summary' in request.form:
            summ = request.form.get('summary')
            summ_dic = {
                "summ" : summ
            }
            update_Book(summ_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))

        if 'form-price' in request.form:
            price = request.form.get('price')
            price_dic = {
                "price": price
            }
            update_Book(price_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))

        if 'form-publisher' in request.form:
            publish = request.form.get('publisher')
            publish_dic = {
                "publisher": publish
            }
            update_Book(publish_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))
            
        if 'form-pageNumber' in request.form:
            page_number = request.form.get('pagenumber')
            number_dic = {
                "page_namber": page_number
            }
            update_Book(number_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))

        if 'form-language' in request.form:
            language = request.form.get('language')
            language_dic = {
                "language_dic" : language
            }
            update_Book(language_dic, book_id)
            return redirect(url_for("updatebook", book_id=book_id))

    return render_template("/updateBook.html", context = res)