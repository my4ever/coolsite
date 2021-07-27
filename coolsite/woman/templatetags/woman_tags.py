from django import template
from woman.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filt=None):
    """Getting categories."""
    if not filt:
        return Category.objects.all()
    else:
        return Category.objects.all(pk=filt)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag
def get_menu():
    menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавте статью', 'url_name': 'add_page'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'}]

    return menu
