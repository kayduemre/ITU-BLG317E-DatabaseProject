from flask.views import View
from flask import render_template, request, url_for, session, redirect
from services.database import Database
from repository.singUpRepository import createUser, findUser
from repository.LibraryRepository import createCategory, getCategorys
from repository.BookRepository import createAuthor, createBook, createPublisher
from repository.CommentRepository import getCommentByBooks, createComment

from models.data.entitiys.UserEntity import UserEntity
from models.data.entitiys.CategoryEntity import CategoryEntity
from models.data.entitiys.Book import Book
from models.data.entitiys.Author import Author
from models.data.entitiys.Publisher import Publisher
from models.data.entitiys.CommentEntity import CommentEntity
import hashlib
from datetime import datetime
class CommentView(View):

    def __init__(self):
        self.book_id = ""

    def dispatch_request(self, **kwargs):

        comment_id = kwargs.get('comment_id')
        print(comment_id)
        self.book_id = comment_id
        comments = getCommentByBooks(comment_id)

        if request.method == 'POST':
            comment = request.form.get('comment')
            vote = request.form.get('vote')
            date = request.form.get('date')
            likeOrDisklike = request.form.get('liordis')

            like = ""
            dislike = ""
            if(likeOrDisklike == "like"):
                like = likeOrDisklike
            elif (likeOrDisklike == "dislike"):
                dislike = likeOrDisklike


            user = session['user']
            name = user[2]+ " " +user[3]
            comment = CommentEntity(comment,vote,like, dislike, name, date, self.book_id)

            createComment(comment)

            
        return render_template("./comments.html", context = comments)