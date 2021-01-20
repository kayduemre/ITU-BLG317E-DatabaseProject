from services.database import Database
from datetime import datetime
from models.data.entitiys.CategoryEntity import CategoryEntity
from psycopg2 import OperationalError, errorcodes, errors
import psycopg2
from flask import session
from repository.BookRepository import getBooks, addBook

def getAllBooks():
    books = getBooks()

    return books

def buy(category_id, book_id, account_id):
    
    addBook(account_id, category_id, book_id)

    db = Database().getDatabaseInstance()
    cursor = db.cursor()
    query = """INSERT INTO BUYYING (BOOK_ID, BUYYING_DATE, USER_ID, ACCOUNT_ID)  VALUES (%(book_id)s, %(buyying_date)s,%(user_id)s,%(account_id)s) RETURNING id"""
    dic = {
        "book_id": book_id,
        "buyying_date": datetime.now(),
        "user_id": account_id,
        "account_id": session['user'][0]
    }
    try:
        cursor.execute(query, dic)
        db.commit()
        author_id =cursor.fetchone()
        print(author_id)
        return author_id
    except psycopg2.Error as e:
        error = e.pgcode
        print(error)
        return error

    return "data"
def barrow(category_id, book_id, account_id):
    addBook(account_id, category_id, book_id)

    db = Database().getDatabaseInstance()
    cursor = db.cursor()
    query = """INSERT INTO BARROWING (BOOK_ID, BARROWING_DATE, USER_ID, ACCOUNT_ID)  VALUES (%(book_id)s, %(buyying_date)s,%(user_id)s,%(account_id)s) RETURNING id"""
    dic = {
        "book_id": book_id,
        "buyying_date": datetime.now(),
        "user_id": account_id,
        "account_id": session['user'][0]
    }
    try:
        cursor.execute(query, dic)
        db.commit()
        author_id =cursor.fetchone()
        print(author_id)
        return author_id
    except psycopg2.Error as e:
        error = e.pgcode
        print(error)
        return error