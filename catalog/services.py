import colorama
from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_cached_subjects_for_product(product_pk):
    if settings.CACHE_ENABLED:
        key = f'subject_list_{product_pk}'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Product.objects.filter(pk=product_pk)
            cache.set(key, subject_list)
    else:
        subject_list = Product.objects.filter(pk=product_pk)

    return subject_list


def log_print_crate_user(user, password):
    print(
        colorama.Fore.GREEN + f'Пользователь создан!\n' + colorama.Fore.RESET + 'login: ' + colorama.Fore.GREEN + f'{user.email}\n' + colorama.Fore.RESET + 'password: ' + colorama.Fore.GREEN + f'{password}' + colorama.Fore.RESET)
