from flask import Blueprint, render_template

chekerpep_bp = Blueprint("chekerpep", __name__)


@chekerpep_bp.route("/chekerpep")
def chekerpep():
    return render_template("chekerpep.html", title="Проверка на pep8"), 200
