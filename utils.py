import json

FILENAME = "candidates.json"


def load_candidates(filename: str) -> list[dict]:
    """Загружаем JSON из файла"""
    with open(filename, encoding='UTF-8') as file:
        return json.load(file)


def get_candidates() -> list[dict]:
    """Получить кандидатов"""
    return load_candidates(FILENAME)


def get_candidates_by_uid(uid: int) -> dict | None:
    """Получить кандидата по UID"""
    candidates = get_candidates()
    for i in candidates:
        if i["id"] == uid:
            return i
    return None


def get_candidates_by_skill(skill: str) -> list[dict]:
    """Получить кандидатов по скилу"""
    candidates = get_candidates()
    result = []
    for i in candidates:
        if skill.lower() in i["skills"].lower().split(", "):
            result.append(i)
    return result


def get_candidates_by_name(name: str) -> list[dict]:
    """Получить кандидатов по имени"""
    candidates = get_candidates()
    result = []
    for i in candidates:
        if name.lower() in i["name"].lower().split(", "):
            result.append(i)
    return result
