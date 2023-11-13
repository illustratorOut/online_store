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
            {'name': 'Апельсин', 'description': 'Оранжевый', 'category': category[0], 'price': 50},
            {'name': 'Огурец', 'description': 'Зеленый', 'category': category[1], 'price': 100},
            {'name': 'Земляника', 'description': 'Красная', 'category': category[2], 'price': 200},
            {'name': 'Авокадо', 'description': 'Зеленый', 'category': category[1], 'price': 300},
            {'name': 'Клубника', 'description': 'Красная', 'category': category[1], 'price': 70},
            {'name': 'Помидор', 'description': 'Красная', 'category': category[2], 'price': 20},
            {'name': 'Лимон', 'description': 'Желтый', 'category': category[0], 'price': 20},
        ]
        Product.objects.bulk_create([Product(**product_item) for product_item in product_list])

        contacts_list = [
            {'country': 'Россия', 'address': 'Мишина ул., 26, Москва этаж 1, помещение 9', 'phone': '89515464951'},
            {'country': 'Германия', 'inn': '847512464', 'address': 'Aue, Schwarzenbergerschtrasse.29',
             'phone': '44-7871234567'},

        ]
        Contacts.objects.bulk_create([Contacts(**contacts_item) for contacts_item in contacts_list])
