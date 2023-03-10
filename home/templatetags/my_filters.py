from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def extract_image_src(html):
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.find('img')
    if img:
        return img['src']
    else:
        return ''