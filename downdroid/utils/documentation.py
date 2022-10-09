import sys
from downdroid.constants import FAIL, ENDC, OKGREEN, UNDERLINE, OKBLUE, WARNING


def documentation():
    print(f"{OKBLUE}{UNDERLINE}command{ENDC}       {OKGREEN}{UNDERLINE}arguments{ENDC}                {WARNING}{UNDERLINE}example{ENDC}\n")
    print(f"{OKBLUE}--help{ENDC}           {OKGREEN}-{ENDC}                     {WARNING}downdroid --help{ENDC}")
    print(f"{OKBLUE}--list{ENDC}    {OKGREEN}releases, versions, all{ENDC}      {WARNING}downdroid --list releases{ENDC}")
    print(
        f"{OKBLUE}--add{ENDC}    {OKGREEN}[version]{ENDC}      {WARNING}downdroid --add android-x86-8.1-r6{ENDC}")

    sys.exit(0)
