from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = '8da77a6e2f5c066e25bac4134fe6e011bf811829df11d999c6409f0a370d3289'    
    # Register application routes via Blueprints
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app
