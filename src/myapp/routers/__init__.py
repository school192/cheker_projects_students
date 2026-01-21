from .main import main_bp
from .chekerpep import chekerpep_bp

def register_routers(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(chekerpep_bp)
