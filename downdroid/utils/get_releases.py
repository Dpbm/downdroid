from downdroid.constants import PROJECT_URL, RELEASES_REF
from requests_html import HTMLSession


def get_releases():
    try:
        session = HTMLSession()
        response = session.get(PROJECT_URL)

        wrapper = response.html.find(RELEASES_REF)

        releases = {}

        for element in wrapper:
            a_tag = element.find('a', first=True)

            link = list(a_tag.absolute_links)[0]
            release_name = a_tag.text

            releases[release_name] = link

        return releases

    except Exception as error:
        print(f'Occured an Error -- {str(error)} -- [get_releases] function')
