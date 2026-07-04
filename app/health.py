from ollama import list


def check_ollama():
    try:
        list()
        return True
    except Exception:
        return False