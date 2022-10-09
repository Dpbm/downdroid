import os

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'

USER = os.environ.get("USER")
HOME = f'/home/{USER}'

DOWNLOADS_DIR = f'{HOME}/Downloads'

PROJECT_URL = "https://osdn.net/projects/android-x86/releases/"


def versions_create_link(
    code): return f'https://osdn.net/ajax/downloads/show_release_item_in.php?release_id={code}&group_id=10312'


RELEASES_REF = "#package-wrap-14990 h4"
