from downdroid.constants import versions_create_link
from downdroid.utils.get_releases import get_releases
from requests_html import HTMLSession


def get_versions():
    try:
        releases = get_releases()
        releases_codes = [release_url.split(
            '/')[-1] for release_url in list(releases.values())]

        versions = {}

        for release_code in releases_codes:
            url = versions_create_link(release_code)

            session = HTMLSession()
            response = session.get(url)

            a_tags = response.html.find('a')

            for a_tag in a_tags:
                version_filename = a_tag.text
                version_name = version_filename.replace('.iso', '')

                if('.iso' in version_filename):
                    link = list(a_tag.absolute_links)[0]
                    versions[version_name] = link

        return versions

    except Exception as error:
        print(f'Occured an Error -- {str(error)} -- [get_versions] function')
