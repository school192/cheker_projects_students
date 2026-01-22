import requests

PATH_GITHUB = "https://github.com/"
PATH_GITHUB_ZIP = "/archive/refs/heads/main.zip"


def get_repository(author, pass_to_github) -> str:
    if pass_to_github[:(len(PATH_GITHUB))] != PATH_GITHUB:
        return "Это не ссылка на github"
    path_download = pass_to_github + PATH_GITHUB_ZIP
    rep = requests.get(path_download)
    if rep.status_code != 200:
        return "Ошибка при получении репозитория"
    with open(f"{author}.zip", "wb") as file:
        file.write(rep.content)
    return f"Репозиторий {author} загружен"


def get_info(data):
    results = []
    for elem in data.splitlines():
        if "\t" not in elem:
            continue
        author = elem.split("\t")[0]
        pass_to_github = elem.split("\t")[1]
        results.append(get_repository(author, pass_to_github))
    return "\n".join(results)

