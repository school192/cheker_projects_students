from flask import Blueprint, render_template

chekerpep_bp = Blueprint("chekerpep", __name__)


@chekerpep_bp.route("/chekerpep")
def cheker():
    return render_template("chekerpep.html", title="Страница проверки pep8"), 200
