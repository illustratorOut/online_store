from django import template

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
