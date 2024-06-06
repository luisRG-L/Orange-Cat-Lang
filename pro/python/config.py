import os

VERBOSE_PROCESS = False
VERBOSE_TOKENS = False
VERBOSE_ACTIONS = False
VERBOSE_MEMORY = False

USER_DIR = os.getenv("USERPROFILE")
if __name__ == "__init__":
    SELECT = os.path.sep
else:
    SELECT = "\\"
ABSOLUTE_PATH = SELECT + "Orange Cat" + SELECT + "Orange-Cat-Lang" + SELECT + "pro"
PROJECTS = USER_DIR + ABSOLUTE_PATH + SELECT + "projects" + SELECT
