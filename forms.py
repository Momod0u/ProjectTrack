from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# Formulaire d'inscription
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(message="Le username est obligatoire."),
        Length(min=3, max=80, message="Entre 3 et 80 caractères.")
    ])
    email = StringField("Email", validators=[
        DataRequired(message="L'email est obligatoire."),
        Email(message="Email invalide.")
    ])
    password = PasswordField("Mot de passe", validators=[
        DataRequired(message="Le mot de passe est obligatoire."),
        Length(min=6, message="Minimum 6 caractères.")
    ])
    confirm_password = PasswordField("Confirmer le mot de passe", validators=[
        DataRequired(),
        EqualTo("password", message="Les mots de passe ne correspondent pas.")
    ])
    submit = SubmitField("S'inscrire")


# Formulaire de connexion
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(message="L'email est obligatoire."),
        Email(message="Email invalide.")
    ])
    password = PasswordField("Mot de passe", validators=[
        DataRequired(message="Le mot de passe est obligatoire.")
    ])
    submit = SubmitField("Se connecter")


# Formulaire de création/modification de projet
class ProjectForm(FlaskForm):
    title = StringField("Titre", validators=[
        DataRequired(message="Le titre est obligatoire."),
        Length(max=255)
    ])
    description = TextAreaField("Description", validators=[
        DataRequired(message="La description est obligatoire.")
    ])
    domaine = StringField("Domaine", validators=[
        DataRequired(message="Le domaine est obligatoire."),
        Length(max=100)
    ])
    statut = SelectField("Statut", choices=[
        ("EN_ATTENTE", "En attente"),
        ("EN_COURS", "En cours"),
        ("TERMINE", "Terminé")
    ])
    submit = SubmitField("Enregistrer")