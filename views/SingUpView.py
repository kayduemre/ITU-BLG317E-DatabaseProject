from flask.views import View
from flask import render_template, request
from models.data.entitiys.UserEntity import UserEntity
from services.database import Database
from repository.singUpRepository import createUser, findUser
import hashlib
class SingUpView(View):

    def __init__(self):
        self.context = {
            "message":"",
            "error": ""
        }

    def get_template_name(self):
        return render_template("./singUp.html", context=self.context)
    
    def createUser(self, name, lastName,email, psw, memberShip):
        return UserEntity(user_name= name, user_last_name= lastName, email= email, password= psw, memberShip= memberShip)

    
    def dispatch_request(self):
        if request.method == 'POST':
            name = request.form.get("name")
            lastName = request.form.get("lName")
            email = request.form.get("email")
            psw = request.form.get("pwd")
            memberShip = request.form.get("membership")
            if memberShip == "option1":
                memberShip = 0
            elif  memberShip == "option2":
                memberShip = 1
            elif  memberShip == "option3":
                memberShip = 2
            
            self.context= {
                "message":"",
                "error": ""
            }
            user = self.createUser(name, lastName, email, hashlib.md5(psw.encode()).hexdigest(), memberShip)
            if findUser(user):
                self.context["error"] = "User already exists."
            else:
                self.context["message"] ="Registration Successful"
                createUser(user)


            return render_template("./singUp.html", context=self.context)
        return self.get_template_name()
