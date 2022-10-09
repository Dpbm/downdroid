import sys
from downdroid.constants import FAIL, ENDC, OKGREEN, UNDERLINE


def argv_error():
    print(f'\n{FAIL}You need  to enter a command!{ENDC}')
    print(f'{OKGREEN}Usage: python3 android.py command [command argument]')
    print(f'To learn more type: {UNDERLINE}python3 android.py --help{ENDC}')
    sys.exit(1)
