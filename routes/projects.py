from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from extensions.sqlalchemy import db
from sqlalchemy import select
from models import Project, StatutType
from forms import ProjectForm

projects_bp = Blueprint("projects", __name__)


# Tableau de bord
@projects_bp.route("/dashboard")
@login_required
def dashboard():
    stmt = select(Project).where(Project.user_id == current_user.id)
    projects = db.session.scalars(stmt).all()

    total = len(projects)
    en_attente = len([p for p in projects if p.statut == StatutType.EN_ATTENTE])
    en_cours = len([p for p in projects if p.statut == StatutType.EN_COURS])
    termine = len([p for p in projects if p.statut == StatutType.TERMINE])

    form = ProjectForm()

    return render_template(
        "projects/dashboard.html",
        projects=projects,
        total=total,
        en_attente=en_attente,
        en_cours=en_cours,
        termine=termine,
        form=form
    )


# Créer un projet
@projects_bp.route("/projects/create", methods=["GET", "POST"])
@login_required
def create():
    form = ProjectForm()

    if form.validate_on_submit():
        new_project = Project(
            title=form.title.data,
            description=form.description.data,
            domaine=form.domaine.data,
            statut=StatutType[form.statut.data],
            user_id=current_user.id
        )
        db.session.add(new_project)
        db.session.commit()

        flash("Projet créé avec succès !", "success")
        return redirect(url_for("projects.dashboard"))

    return render_template("projects/create.html", form=form)


# Modifier un projet
@projects_bp.route("/projects/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def edit(project_id):
    project = db.session.scalar(
        select(Project).where(Project.id == project_id)
    )

    if project is None:
        abort(404)

    if project.user_id != current_user.id:
        abort(403)

    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        project.title = form.title.data
        project.description = form.description.data
        project.domaine = form.domaine.data
        project.statut = StatutType[form.statut.data]
        db.session.commit()

        flash("Projet modifié avec succès !", "success")
        return redirect(url_for("projects.dashboard"))

    return render_template("projects/edit.html", form=form, project=project)


# Supprimer un projet
@projects_bp.route("/projects/<int:project_id>/delete", methods=["POST"])
@login_required
def delete(project_id):
    project = db.session.scalar(
        select(Project).where(Project.id == project_id)
    )

    if project is None:
        abort(404)

    if project.user_id != current_user.id:
        abort(403)

    db.session.delete(project)
    db.session.commit()

    flash("Projet supprimé.", "info")
    return redirect(url_for("projects.dashboard"))