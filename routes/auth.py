from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from extensions.sqlalchemy import db
from sqlalchemy import select
from models import User
from forms import RegisterForm, LoginForm

# Création du blueprint
auth_bp = Blueprint("auth", __name__)


# Route d'inscription
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Vérifier si l'email existe déjà
        existing_user = db.session.scalar(
            select(User).where(User.email == form.email.data)
        )
        if existing_user:
            flash("Cet email est déjà utilisé.", "danger")
            return redirect(url_for("auth.register"))

        # Créer le nouvel utilisateur
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Compte créé avec succès. Connecte-toi !", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


# Route de connexion
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Chercher l'utilisateur par email
        user = db.session.scalar(
            select(User).where(User.email == form.email.data)
        )

        # Vérifier si l'utilisateur existe et si le mot de passe est correct
        if user is None or not check_password_hash(user.password, form.password.data):
            flash("Email ou mot de passe incorrect.", "danger")
            return redirect(url_for("auth.login"))

        # Connecter l'utilisateur
        login_user(user)
        flash("Bienvenue " + user.username + " !", "success")
        return redirect(url_for("projects.dashboard"))

    return render_template("auth/login.html", form=form)


# Route de déconnexion
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Tu es déconnecté.", "info")
    return redirect(url_for("auth.login"))