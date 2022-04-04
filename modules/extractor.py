from bs4 import BeautifulSoup
from bs4.element import Comment


def titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles_list = soup.find_all(attrs={"title": True})
    titles_values = ""
    for title in titles_list:
        titles_values += title["title"].lower()
    return titles_values


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text(html):
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip().lower() for t in visible_texts)
