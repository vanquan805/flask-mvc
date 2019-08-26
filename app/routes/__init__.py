from . import home


def create_router(app):
    app.register_blueprint(home.router_home)
