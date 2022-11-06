from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from elasticsearch import Elasticsearch

from config import Config

db = SQLAlchemy()
migrate = Migrate()
es = Elasticsearch(
    hosts=[
        {
            'host': Config.ELASTICSEARCH_HOST, 
            'port': 9200,
            'scheme': 'http'
        }
    ],
    timeout=30
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    CORS(
        app,
        allow_headers=[
            "Content-Type",
            "Authorization",
            "Access-Control-Allow-Credentials"
        ],
        origins="*",
        supports_credentials=True
    )

    from app.views import blueprint as views_bp
    app.register_blueprint(views_bp)

    return app
