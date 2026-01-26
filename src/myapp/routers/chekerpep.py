from flask import Blueprint, render_template, request
from myapp.utils.get_reps import get_info

chekerpep_bp = Blueprint("chekerpep", __name__)


@chekerpep_bp.route("/chekerpep", methods=['GET', 'POST'])
def chekerpep():
    if request.method == 'GET':
        return render_template("chekerpep.html", title="Проверка на pep8"), 200
    result = get_info(request.form.get('list_reps'))
    return render_template("chekerpep.html", title="Проверка на pep8", results=result), 200


@chekerpep_bp.route("/chekerpep/results", methods=['GET'])
def chekerpep_results():
    if request.method == 'GET':
        return render_template("chekerpepresults.html", title="Результаты проверки на pep8"), 200
    result = "Тут будет результаты работы проверки"
    return render_template("chekerpepresults.html", title="Результаты проверки на pep8", results=result), 200

