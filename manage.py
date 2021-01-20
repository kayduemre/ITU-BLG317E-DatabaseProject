from flask import Flask, session
import psycopg2
import os
# from model.user.UserDatabase import UserDatabase
from controllers.Controller import Controller
from flask_login import LoginManager
# from model.user.UserModel import UserModel
# from view.singIn import SingInView
# from controllers.singInController.SingInController import SingInController
# from view.singUp import SingUpView
# from controllers.singUpController.SingUpController import SingUpController
loginManager = LoginManager()


@loginManager.user_loader
def load_user(user_id):
     return get_user(user_id)

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    loginManager.init_app(app)
    loginManager.login_view = "SingInView"
    
    

    Controller(app).initialRouter()

    # lm.init_app(app)
    # lm.login_view = "login_page"

    
    # home_dir = os.path.expanduser("~")
    # db_host = "localhost"
    # db_port = 5432
    # db_name = "sharebook"
    # db_user = "emre"
    # db_pass = "emre6549"
    # conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pass, port=db_port)
    
    # cursor = conn.cursor()
    # conn.close()
    # postgreSQL_select_Query = "select id from beauticians where first_name = %s"
    
    app.config['TESTING'] = False
    if session:
        print(session['user'])

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)