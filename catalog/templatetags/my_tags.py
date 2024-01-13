from django import template

from catalog.models import Product

register = template.Library()


# Создание тега
@register.simple_tag
def mediapath(format_string):
    print(format_string)
    return f'/media/{format_string}'


# Создание фильтра
@register.filter()
def mediapath(text):
    return f'/media/{text}'


# Создание тега кол-во продуктов в категории!
@register.filter()
def category_qty_product(format_string):
    res = Product.objects.filter(category=format_string).count()
    return res
