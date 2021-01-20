from flask.views import View
from flask import render_template, request, url_for, session, redirect
from services.database import Database
from repository.UserRepository import getUsers, sendFeedBack
from models.data.entitiys.FeedBack import FeedBack

import hashlib
from datetime import datetime

class UsersView(View):

    def dispatch_request(self,**kwargs):
        users = getUsers()
        userList = []
        for user in users:
            dic = {
                "id": user[1],
                "name": user[2] +" "+ user[3],
                "email": user[4]
            }
            userList.append(dic)

        if kwargs:

            if request.method == "POST":
                protect = request.form.get('protect')
                reliability = request.form.get('reliability')
                delivery = request.form.get('Delivery')
                user_id = kwargs.get("user_id")

                feedback = FeedBack(user_id,protect, reliability,delivery)
                sendFeedBack(feedback)
                print(feedback.dic())

                
            return render_template("/feedbackUser.html")
        return render_template("/users.html", context = userList)