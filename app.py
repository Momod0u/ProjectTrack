import json
from flask import Flask
from extensions.sqlalchemy import db
from extensions.migrate import migrate
from extensions.login import login_manager

# Création de l'application Flask
app = Flask(__name__)

# Chargement de la config depuis config.json
app.config.from_file("config.json", load=json.load)

# Initialisation des extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

# Enregistrement des blueprints
from routes.auth import auth_bp
from routes.projects import projects_bp

app.register_blueprint(auth_bp)
app.register_blueprint(projects_bp)

if __name__ == "__main__":
    app.run(debug=True)