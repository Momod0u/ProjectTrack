import enum
from datetime import datetime, timezone
from sqlalchemy import String, Boolean, DateTime, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column
from extensions.sqlalchemy import db
from flask_login import UserMixin


class StatutType(enum.Enum):
    EN_ATTENTE = "En attente"
    EN_COURS = "En cours"
    TERMINE = "Terminé"


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relation 1-N : un user a plusieurs projets
    projects: Mapped[list["Project"]] = db.relationship(
        back_populates="owner",
        cascade="all, delete-orphan"
    )


class Project(db.Model):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    domaine: Mapped[str] = mapped_column(String(100))
    statut: Mapped[StatutType] = mapped_column(
        Enum(StatutType),
        default=StatutType.EN_ATTENTE
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Clé étrangère vers User
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))

    # Relation inverse
    owner: Mapped["User"] = db.relationship(back_populates="projects")