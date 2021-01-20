from flask.views import View
from flask import render_template, request, url_for, session, redirect
from services.database import Database
from repository.singUpRepository import createUser, findUser
from repository.LibraryRepository import createCategory, getCategorys
from repository.BookRepository import getbooksBycategory, deleteBookById

from models.data.entitiys.UserEntity import UserEntity
from models.data.entitiys.CategoryEntity import CategoryEntity
import hashlib
from datetime import datetime
class LibraryView(View):

    def __init__(self,**kwargs):
        self.category_id = kwargs.get('category_id')
        self.erorFlag = 1
        self.categorys = []
    

    def dispatch_request(self,**kwargs):
        
        if request.method == 'POST':
            title = request.form.get('title')
            user = session.pop('user',None)
            session['user'] = user
            accountId = user[1]
            date = datetime.now()
            print(date.strftime('%Y-%m-%d'))

            data = CategoryEntity(title, accountId, date)
            response = createCategory(data)
            if response == 0:
                self.erorFlag = 0
            else:
                self.categorys = getCategorys(session['user'][1])
        else:
            self.categorys = getCategorys(session['user'][1])

        if self.erorFlag == 0:
            error = {
                "message": "Category names must be different",
                "flag": 0
            }
            content = error
        else:
            category_id = kwargs.get('category_id')
            categorysList = []
            books = getbooksBycategory(category_id)
            
            bookList = []
            for row in books:
                book = {}
                book['id'] = row[0]
                book['comment_id'] = row[1]
                book['title'] = row[2]
                book['author'] = row[3]
                book['summary'] = row[4]
                book['publisher'] = row[5]
                book['page_number'] = row[6]
                book['language'] = row[7]
                book['vote'] = row[9]
                book['price'] = row[10]
                bookList.append(book)

            for row in self.categorys:
                categorysList.append(row)

            content = {
                "flag" : 1,
                "data": categorysList,
                "books": bookList
            }
        
        if kwargs.get('book_id'):
            book_id = kwargs.get('book_id')
            deleteBookById(book_id)

            
        return render_template("./books.html", context = content)

