#!/bin/python3
import sys
from downdroid.utils.get_releases import get_releases
from downdroid.utils.argv_error import argv_error
from downdroid.utils.argument_error import argument_error
from downdroid.utils.documentation import documentation
from downdroid.utils.get_versions import get_versions
from downdroid.utils.download_file import download_file
from downdroid.constants import OKGREEN, ENDC


def get(argument):
    try:
        releases = get_releases()

        if(argument == 'releases' or argument == 'all'):

            print(f'\n{OKGREEN}Found Releases: {ENDC}\n')
            for release in releases:
                print(f'{release}')

        if(argument == 'versions' or argument == 'all'):
            print(f'\n{OKGREEN}Found versions: {ENDC}\n')

            versions = get_versions()

            for version in versions:
                print(f'{version}')

    except Exception as error:
        print(f'Occured an Error -- {str(error)} -- [get] function')


commands = {
    "--help": {
        'function': documentation,
        'total_arguments': 0,
        'accepted_arguments': []
    },

    "--list": {
        'function': get,
        'total_arguments': 1,
        'accepted_arguments': ['all', 'versions', 'releases']
    },

    "--add": {
        'function': download_file,
        'total_arguments': 1,
        'accepted_arguments': []
    }
}


def main():
    try:
        arguments = sys.argv

        if(len(arguments) <= 1):
            argv_error()

        selected_command = arguments[1]
        command_data = commands[selected_command]
        command = command_data['function']

        if(not command_data['total_arguments']):
            command()

        command_argument = arguments[2]

        if(command_argument not in command_data['accepted_arguments'] and command_data['accepted_arguments']):
            argument_error()

        command(command_argument)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
