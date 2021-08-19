from flask import Flask

def create_app():
    app = Flask(
        __name__,
        static_folder=None
    )

    from .views import views
    app.register_blueprint(views)

    return app