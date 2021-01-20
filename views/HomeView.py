from flask.views import View
from flask import render_template, request,redirect,url_for, session
from repository.HomePageRepository import getAllBooks, buy, barrow
from repository.LibraryRepository import getCategorys
class HomeView(View):

    def __init(self):
        self.categorys = []

    def dispatch_request(self):
        categorysList = []
        categorys = getCategorys(session['user'][1])
        books = getAllBooks()
        print("users",session['user'])
        categoryList = []
        for row in categorys:
            dic = {}
            dic['id'] = row[0]
            dic['name'] = row[3]
            dic['account_id'] = row[4]
            categoryList.append(dic)
            del dic
        
        
        bookList = []
        for row in books:
            book = {}
            book['id'] = row[0]
            book['title'] = row[2]
            book['author'] = row[3]
            book['summary'] = row[4]
            book['publisher'] = row[5]
            book['page_number'] = row[6]
            book['language'] = row[7]
            book['vote'] = row[8]
            book['price'] = row[10]
            bookList.append(book)
        
        
        content = {
            "flag" : 1,
            "books": bookList,
            "category": categoryList
        }

        return render_template("/home.html", context = content)
def buyBook(**kwargs):
    category_id = kwargs.get('category_id')
    account_id =kwargs.get('account_id')
    book_id = kwargs.get('book_id')
    response = buy(category_id, book_id, account_id)
    
    return redirect(url_for('home'))
def barrowBook(**kwargs):
    account_id = kwargs.get('account_id')
    category_id = kwargs.get('category_id')
    book_id = kwargs.get('book_id')
    response = barrow(category_id,book_id, account_id)
    
    return redirect(url_for('home'))