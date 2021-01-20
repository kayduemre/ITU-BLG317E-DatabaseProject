from flask.views import View
from flask import render_template, request, url_for, session, redirect
from services.database import Database
from repository.singUpRepository import createUser, findUser
from models.data.entitiys.UserEntity import UserEntity
import hashlib

class SingInView(View):
    def __init__(self):
        self.context = {
            "error": ""
        }

    def dispatch_request(self):
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('pwd')
            

            user = UserEntity(email=email,password=password)
            findedUser = findUser(user)
            if (findUser):
                if(findedUser[4] == email and findedUser[5] == hashlib.md5(password.encode()).hexdigest() ):
                    session['user'] = findedUser
                    return redirect(url_for('home'))
                else:
                    message = "Email or password is incorrect"
                    return render_template("./login.html", message=message )
            else:
                message = "Email or password is incorrect"
                return render_template("./login.html", message="")
        return render_template("./login.html", message="")

def logOut():
    session.pop('user', None)
    return redirect(url_for('login'))
