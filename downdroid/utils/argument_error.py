import sys
from downdroid.constants import FAIL, ENDC, UNDERLINE, OKGREEN


def argument_error():
    print(f'\n{FAIL}Invalid argument!{ENDC}')
    print(f'{OKGREEN}To learn more type: {UNDERLINE}python3 android.py --help{ENDC}')
    sys.exit(1)
