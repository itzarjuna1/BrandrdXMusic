import os

from ..logging import LOGGER

BASE_DIR = os.getcwd()
BACKUP_DIR = os.path.join(BASE_DIR, "ASTRALBACKUP")

os.makedirs(BACKUP_DIR, exist_ok=True)


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")

    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Directories Updated.")
