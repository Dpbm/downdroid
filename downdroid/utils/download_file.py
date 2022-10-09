from downdroid.constants import DOWNLOADS_DIR
from urllib.request import urlretrieve
from downdroid.utils.get_version_url import get_version_url
from requests_html import HTMLSession
from tqdm import tqdm
import os


def count_progress(t):
    last_b = [0]

    def update_to(b=1, bsize=1, tsize=None):
        if tsize is not None:
            t.total = tsize

        t.update((b - last_b[0]) * bsize)

        last_b[0] = b

    return update_to


def download_file(version, target_directory=DOWNLOADS_DIR):
    try:
        url = get_version_url(version)

        if(url):
            session = HTMLSession()
            response = session.get(url)
            p_element = response.html.find('p', first=True)
            download_link = list(p_element.absolute_links)[0]

            if(download_link):
                target_file = f'{target_directory}/{version}.iso'

                with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=target_file) as t:
                    urlretrieve(download_link, target_file,
                                reporthook=count_progress(t), data=None)

                os.system(f'rm -rf {target_file}.crdownload')
                print('Done :)')
                return

        raise Exception('Error on get file')

    except Exception as error:
        print(f'Occured an Error -- {str(error)} -- [download_file] function')
