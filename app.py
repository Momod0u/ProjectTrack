import json
from flask import Flask, redirect, url_for
from extensions.sqlalchemy import db
from extensions.migrate import migrate
from extensions.login import login_manager

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

from routes.auth import auth_bp
from routes.projects import projects_bp

app.register_blueprint(auth_bp)
app.register_blueprint(projects_bp)

@app.route("/")
def index():
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)