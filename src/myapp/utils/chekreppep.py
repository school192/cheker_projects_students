import zipfile

import pep8


def unziprep(author: str) -> str:
    """Распаковка репозитория."""
    with zipfile.ZipFile(f"data/{author}.zip", 'r') as zip_ref:
        zip_ref.extractall(f"data/{author}")
    return f"Репозиторий {author} распакован"

def chekreppep(author: str) -> str:
    """Проверка репозитория на pep8."""
    # Заглушка для проверки pep8

    return f"Репозиторий {author} проверен на pep8"


code_to_be_checked = """

x = 123

"""

fchecker = pep8.Checker(lines=code_to_be_checked, show_source=True)
errors = fchecker.check_all()

print("PEP8 error count: {}".format(errors))
