from flask import Flask
from views.SingUpView import SingUpView
from views.SingInView import SingInView, logOut
from views.HomeView import HomeView, barrowBook, buyBook
from views.LibraryView import LibraryView
from views.BookView import BookView, updateBook
from views.CommentView import CommentView
from views.UsersView import UsersView

class Controller:

    def __init__(self, app):
        self.app = app
        self.user_view = SingUpView.as_view('singup')
        self.login_view = SingInView.as_view('login')
        self.home_view = HomeView.as_view('home')
        self.library_view = LibraryView.as_view('library')
        self.DeleteBook_view = LibraryView.as_view('deletebook')
        self.Book_view = BookView.as_view('book')
        self.Comments_view = CommentView.as_view('comments')
        self.Users_view = UsersView.as_view('user')
        self.FeedBack_view = UsersView.as_view('feedback')

    def initialRouter(self):
        
        self.app.add_url_rule('/singup/', view_func=self.user_view, methods=["GET", "POST"])
        self.app.add_url_rule('/login', view_func=self.login_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/logOut', view_func=logOut)
        self.app.add_url_rule('/user', view_func=self.Users_view, methods=['GET', "POST"])
        self.app.add_url_rule('/user/<int:user_id>', view_func=self.Users_view, methods=['GET', "POST"])

        self.app.add_url_rule('/', view_func=self.home_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/home', view_func=self.home_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/buy/<int:category_id>/<int:account_id>/<int:book_id>','buy', view_func=buyBook, methods=['GET', 'POST'])
        self.app.add_url_rule('/barrow/<int:category_id>/<int:account_id>/<int:book_id>','barrow', view_func=barrowBook, methods=['GET', 'POST'])
        

        self.app.add_url_rule('/library/', view_func=self.library_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/library/<int:category_id>/', view_func=self.library_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/comments/<int:comment_id>/', view_func=self.Comments_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/book', view_func=self.Book_view, methods=['GET', 'POST'])
        self.app.add_url_rule('/book/update/<int:book_id>', 'updatebook', view_func=updateBook, methods=['GET', 'POST'])
        self.app.add_url_rule('/book/delete/<int:book_id>', view_func=self.DeleteBook_view, methods=['GET', 'POST'])