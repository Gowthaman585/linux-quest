from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register application routes via Blueprints
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app
