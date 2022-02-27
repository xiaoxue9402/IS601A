from django.shortcuts import render
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Create your views here.
book = epub.read_epub('epubpower_app/Neverwhere A Novel by Neil Gaiman (z-lib.org).epub')
chapters = book.get_items()
texts = {}
def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = soup.text
    return ''.join(text)
for c in chapters:
    if c.get_type() == ebooklib.ITEM_DOCUMENT:
        texts[c.get_name()] = [chapter_to_str(c)]

def index(request):
    print(texts)
    return render(request, 'index.html', {
        'book': book,
        'items': texts
    })
