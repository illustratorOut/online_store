from datetime import datetime

from django.core.management import BaseCommand
from blog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        Blog.truncate()

        blog_list = [
            {'title': 'Апельсин',
             'slug': 'apelsin',
             'body': 'Апельсин — самая распространённая цитрусовая культура во всех тропических и субтропических областях мира. Существует предположение о происхождении как гибрида мандарина (Citrus reticulata) и помело (Citrus maxima).',
             'preview': 'product/Апельсин.png',
             'date_create': datetime.now(),
             'is_published': True,
             'count_views': 0},

            {'title': 'Огурец',
             'slug': 'ogurec',
             'body': 'Огурцы — это плоды однолетнего травянистого растения семейства Тыквенные. Относятся к овощным культурам. Плоды располагаются на длинном стелющемся шершавом стебле, который в длину может достигать 2 метров. ',
             'preview': 'product/Огурец.jpg',
             'date_create': datetime.now(),
             'is_published': True,
             'count_views': 0},

            {'title': 'Лимон',
             'slug': 'limon',
             'body': 'Лимон – это многолетнее вечнозеленое плодовое дерево высотой в среднем 4 - 7 м, живет примерно 40 лет. Начинает цвести дерево еще весной, а осенью плоды созревают. Плод л. имеет овальную форму длиной 6-9 см, светло-желтого цвета с бугорчатой коркой. Родиной этого фрукта предположительно считается Северная Индия или Бирма. Культивируется в странах с субтропическим климатом. Также распространен в комнатной культуре. Плод л. называют - гесперидий.',
             'preview': 'product/Лимон.png',
             'date_create': datetime.now(),
             'is_published': True,
             'count_views': 0},

            {'title': 'Авокадо',
             'slug': 'avokado',
             'body': 'Авокадо (крокодилова или аллигаторова груша) — это фрукт или даже скорее однокосточковая ягода. В быту из-за отсутствия сладости его часто относят к овощам. Но всё-таки эти плоды растут на деревьях, что нехарактерно для овощей.',
             'preview': 'product/Авокадо.png',
             'date_create': datetime.now(),
             'is_published': False,
             'count_views': 0},
        ]
        Blog.objects.bulk_create([Blog(**blog_item) for blog_item in blog_list])
