from django.core.management import BaseCommand
from catalog.models import Category, Product, Contacts


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.truncate()
        Category.truncate()
        Contacts.truncate()

        category_list = [
            {'name': 'Фрукты', 'description': 'Сладкие'},
            {'name': 'Овощи', 'description': 'Зрелые'},
            {'name': 'Ягоды', 'description': 'Спелые'}
        ]
        Category.objects.bulk_create([Category(**category_item) for category_item in category_list])

        category = Category.objects.all()
        product_list = [
            {'name': 'Апельсин', 'description': 'Оранжевый', 'category': category[0], 'price': 50,
             'photo': 'product/Апельсин.png'},

            {'name': 'Огурец',
             'description': 'Огурцы — это плоды однолетнего травянистого растения семейства Тыквенные. Относятся к овощным культурам. Плоды располагаются на длинном стелющемся шершавом стебле, который в длину может достигать 2 метров. ',
             'category': category[1], 'price': 100,
             'photo': 'product/Огурец.jpg'},

            {'name': 'Земляника',
             'description': 'Земляника – травянистое растение с мочковатой корневой системой, основная масса корней которой проникает на глубину 20-25 см. Листья сложные, тройчатые, сидят на длинных стебельках. Побеги ползучие, быстро укореняющиеся. Цветки некрупные, обоеполые, собраны в многоцветковые щитки, расположены на длинных цветоносах, формирующихся в форме розетки от корневой шейки. Лепестки белые, реже желтоватые.',
             'category': category[2], 'price': 200,
             'photo': 'product/Земляника.jpg'},

            {'name': 'Авокадо',
             'description': 'Авокадо — это мясистый плод с вечнозеленого дерева, произрастающего в Центральной Америке. На родине он известен как «аллигаторова груша». По форме он и правда похож на грушу, а снаружи покрыт грубой шероховатой кожурой зеленого цвета. По вкусу авокадо чем–то напоминает сливочное масло с зеленью и легким ореховым привкусом.',
             'category': category[0], 'price': 300,
             'photo': 'product/Авокадо.jpg'},

            {'name': 'Клубника',
             'description': 'Ее жизненная форма – травы, класс – двудольные, род – земляника. Строение куста очень простое. Он состоит из корневой системы, листьев, усиков, цветоноса и небольшого однолетнего рожка. Ягода распространена как в Европе, так и в Азии. ',
             'category': category[2], 'price': 70,
             'photo': 'product/Клубника.jpg'},

            {'name': 'Помидор', 'description': 'Красный какой-то текст для заполнения контента', 'category': category[1], 'price': 20,
             'photo': 'product/Помидор.png'},

            {'name': 'Лимон',
             'description': 'Лимон – это многолетнее вечнозеленое плодовое дерево высотой в среднем 4 - 7 м, живет примерно 40 лет. Начинает цвести дерево еще весной, а осенью плоды созревают. Плод л. имеет овальную форму длиной 6-9 см, светло-желтого цвета с бугорчатой коркой. Родиной этого фрукта предположительно считается Северная Индия или Бирма. Культивируется в странах с субтропическим климатом. Также распространен в комнатной культуре. Плод л. называют - гесперидий.',
             'category': category[0], 'price': 20, 'photo': 'product/Лимон.png'},
        ]
        Product.objects.bulk_create([Product(**product_item) for product_item in product_list])

        contacts_list = [
            {'country': 'Россия', 'address': 'Мишина ул., 26, Москва этаж 1, помещение 9', 'phone': '89515464951'},
            {'country': 'Германия', 'inn': '847512464', 'address': 'Aue, Schwarzenbergerschtrasse.29',
             'phone': '44-7871234567'},

        ]
        Contacts.objects.bulk_create([Contacts(**contacts_item) for contacts_item in contacts_list])
