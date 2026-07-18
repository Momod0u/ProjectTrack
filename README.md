# ProjectTrack 

Application web de suivi de projets étudiants développée avec Flask.

## Technologies utilisées

- Python 3.14
- Flask 3.1.3
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.1.0
- Flask-Login 0.6.3
- Flask-WTF 1.2.2
- SQLite
- Glassmorphism CSS Design

## Fonctionnalités

- Inscription et connexion sécurisée
- Tableau de bord personnel
- Création, modification et suppression de projets
- Statuts : En attente / En cours / Terminé
- Interface moderne Glassmorphism

## Installation

### 1. Cloner le projet

git clone https://github.com/Momod0u/ProjectTrack.git
cd ProjectTrack


### 2. Créer et activer l'environnement virtuel

python -m venv venv
venv\Scripts\Activate.ps1


### 3. Installer les dépendances

pip install -r requirements.txt


### 4. Initialiser la base de données

flask --app app db upgrade


### 5. Lancer l'application

flask --app app run --debug


### 6. Ouvrir dans le navigateur

http://127.0.0.1:5000


## Comptes de test

| Username | Email | Mot de passe |
|----------|-------|--------------|
| momod | momod@test.com | 123456 |

## Auteur

Mamadou Racine BA — Licence 2 DSBD — ISI Sénégal 2025-2026