CURRENT_COURSE_FILE = "/home/jovyan/library/.current_course"

def read_current_course():
    try:
        with open(CURRENT_COURSE_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def write_current_course(course):
    with open(CURRENT_COURSE_FILE, "w") as f:
        f.write(course)
