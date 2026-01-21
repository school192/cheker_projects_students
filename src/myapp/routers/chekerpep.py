from flask import Blueprint, render_template, request

chekerpep_bp = Blueprint("chekerpep", __name__)


@chekerpep_bp.route("/chekerpep", methods=['GET', 'POST'])
def chekerpep():
    if request.method == 'GET':
        return render_template("chekerpep.html", title="Проверка на pep8"), 200
    print(request.form.get('list_reps'))
    return ''
