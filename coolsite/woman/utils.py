from django.db.models.aggregates import Count
from django.core.cache import cache

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавте статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))
            cache.set('cats', cats, 60)

        user_meny = menu.copy()
        if not self.request.user.is_authenticated:
            user_meny.pop(1)
        context['menu'] = user_meny
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context