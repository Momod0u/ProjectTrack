from flask_login import LoginManager

login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Connecte-toi pour accéder à cette page."

@login_manager.user_loader
def load_user(user_id):
    from models import User
    from extensions.sqlalchemy import db
    from sqlalchemy import select

    return db.session.scalar(select(User).where(User.id == int(user_id)))