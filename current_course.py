CURRENT_FILE = "/home/jovyan/library/.current_course"


def read_current_course():
    try:
        with open(CURRENT_FILE, "r") as f:
            data = f.read().strip()
            return data
    except FileNotFoundError:
        return None, None, None


def write_current_course(data):
    with open(CURRENT_FILE, "w") as f:
        f.write(data)
