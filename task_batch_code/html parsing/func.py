
import html, os
from bs4 import BeautifulSoup


def read_html_contents_to_str(source, tag='', attrs={}):
    """
    :param source: source of html. filepath or html string
    :param tag: tag selection expression

    :return: selected tag from html contents to string
    """
    assert isinstance(source,str), 'source args should be str type, but {0}'.format(type(source))
    assert isinstance(tag, str), 'tag kwargs should be str type, but {0}'.format(type(tag))
    assert tag != '', 'tag kwargs should not be empty str'
    assert isinstance(attrs, dict), 'attr kwargs should be dict type, but {0}'.format(type(attrs))

    if os.path.exists(source):  # is source is a file path
        content = open(source, 'r').read()
        soup = BeautifulSoup(content, 'lxml')

    else:   # source is a html string
        soup = BeautifulSoup(source, 'lxml')

    selected_html_str = str(soup.find(tag, attrs=attrs))

    return selected_html_str


def write_replace_html_contents(source, replace_values={}, write_to=''):
    """
    replace html contents from given source & write to html file

    :param source: source html. filepath or html_string
    :param replace_values: replace value contents with dictionary type
    :param write_to: output html filepath
    :return: html string which replace html contents from given source
    """
    assert isinstance(write_to, str), 'write_to kwargs should be str type, but {0}'.format(type(write_to))

    html_string = replace_html_contents(source, replace_values=replace_values)

    with open(write_to, 'w') as file:
        file.write(html_string)

    return html_string


def replace_html_contents(source, replace_values={}):
    """
    replace html contents from given source

    :param source: source html. filepath or html_string
    :param replace_values: replace value contents with dictionary type
    :return: html string which replace html contents from given source
    """
    assert isinstance(source, str), 'source kwargs should be str type, but {0}'.format(type(source))
    assert isinstance(replace_values, dict), 'replace_values kwargs should be dict type, but {0}'.format(type(replace_values))
    assert replace_values != {}, 'replace_values kwargs should not be empty dict, but {0}'.format(type(replace_values))

    if os.path.exists(source):  # is source is a file path
        content = open(source, 'r').read()
        soup = BeautifulSoup(content, 'lxml')

    else:   # source is a html string
        soup = BeautifulSoup(source, 'lxml')

    for key, val in replace_values.items():
        _replace_html_contents(soup, tag=val['tag'], attrs=val['attrs'], replace_value=val['replace_value'])

    soup_unescaped = html.unescape(str(soup))  # unescaped html_string

    return soup_unescaped


def _replace_html_contents(soup, tag='', attrs={}, replace_value=''):
    """
    replace html content from given source

    :param soup: bs4 soup class
    :param tag: tag selector
    :param attrs: attrs selector
    :param replace_value: replace value
    :return: soup object which has replaced value
    """

    assert isinstance(tag, str), 'tag kwargs should be str type, but {0}'.format(type(tag))
    assert tag != '', 'tag kwargs should not be empty str'
    assert isinstance(attrs, dict), 'attr kwargs should be dict type, but {0}'.format(type(attrs))
    assert isinstance(replace_value, str), 'replace_value kwargs should be str type, but {0}'.format(type(replace_value))
    assert replace_value != '', 'replace_value kwargs should not be empty str'

    selected_html = soup.find(tag, attrs=attrs)
    selected_html.string = replace_value
