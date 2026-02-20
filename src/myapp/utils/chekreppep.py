import zipfile
import flake8
import os

def unziprep(author: str) -> str:
    """Распаковка репозитория."""
    with zipfile.ZipFile(f"data/{author}.zip", 'r') as zip_ref:
        zip_ref.extractall(f"data/{author}")
    return f"Репозиторий {author} распакован"


def chekreppep(author: str) -> str:
    """Проверка репозитория на pep8."""
    # Заглушка для проверки pep8
    path_to_repo = f"data/{author}_unzipped"
    os.system(f"cd {path_to_repo} && flake8 . > files_to_check.txt")
    os.system(f"cd {path_to_repo} && find . -name *.py ")
    with open(f"{path_to_repo}/files_to_check.txt", "r") as f:
        details = f.readlines()
    if not details:
        details = ["Ошибок не найдено"]
    results = (author, "Тут будет статус", details)
    return results


def start_chekreppep() -> str:
    """Запуск проверки репозитория на pep8."""
    list_dirs_authors = os.listdir("data")
    results = []
    for author in list_dirs_authors:
        if author.endswith("_unzipped"):
            results.append(chekreppep(author.replace("_unzipped", "")))
    return results


