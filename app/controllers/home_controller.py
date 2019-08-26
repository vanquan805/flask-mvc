# from app import database
# from app.models import User
from flask import render_template

def index():
    # user = User.User(email="vanquan805@gmail.com", username="vanquan805", first_name="Nguyen", last_name="Quan",
    #                  password="12356")
    # database.session.add(user)
    # database.session.commit()
    return render_template('components.html')
