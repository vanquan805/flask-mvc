from flask import render_template, Blueprint
from app.controllers import home_controller

router_home = Blueprint('home', __name__, url_prefix='/')

router_home.add_url_rule('/', 'home', home_controller.index)
