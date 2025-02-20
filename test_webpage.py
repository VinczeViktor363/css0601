import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def load_html():
    with open("index.html", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def test_html_structure(load_html):
    assert load_html.html is not None, "Az oldalnak lennie kell egy <html> elemnek."
    assert load_html.head is not None, "Az oldalnak lennie kell egy <head> elemnek."
    assert load_html.body is not None, "Az oldalnak lennie kell egy <body> elemnek."

def test_title(load_html):
    title = load_html.title
    assert title is not None, "Az oldalnak lennie kell egy <title> elemnek."
    assert title.string == "Alaszka", "A címnek 'Alaszka' kell lennie."

def test_stylesheet_link(load_html):
    link = load_html.find("link", {"rel": "stylesheet"})
    assert link is not None, "Hiányzik a CSS fájl kapcsolódása."
    assert link["href"] == "style.css", "A CSS fájl neve nem megfelelő."

def test_content_exists(load_html):
    content_div = load_html.find("div", class_="content")
    assert content_div is not None, "Hiányzik a fő tartalmi div."

def test_main_heading(load_html):
    h1 = load_html.find("h1")
    assert h1 is not None, "Az oldalnak lennie kell egy <h1> elemnek."
    assert h1.string.strip() == "Alaszka", "A főcímnek 'Alaszka'-nak kell lennie."

def test_paragraphs(load_html):
    paragraphs = load_html.find_all("p")
    assert len(paragraphs) >= 3, "Legalább 3 bekezdésnek kell lennie az oldalon."

def test_highlighted_section(load_html):
    highlighted = load_html.find("span", class_="hatarok")
    assert highlighted is not None, "Hiányzik a kiemelt szövegrész."
    assert "Kanadával" in highlighted.text, "A kiemelt részben szerepelnie kell 'Kanadával'-nak."

def test_source_link(load_html):
    link = load_html.find("a", href="https://hu.wikipedia.org/wiki/Alaszka")
    assert link is not None, "Hiányzik a Wikipédia forráshivatkozás."
    assert link.text.strip() == "hu.wikipedia.org", "A link szövege nem megfelelő."

def test_background_image():
    with open("style.css", encoding="utf-8") as f:
        css_content = f.read()
    assert "state_seal_of_alaska.png" in css_content, "A háttérkép nincs megfelelően beállítva."

