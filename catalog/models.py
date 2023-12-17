from django.conf import settings
from django.db import models, connection
import colorama

NULLABLE = {'null': True, 'blank': True}


class Truncate:
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            name_table = f'{cls.__module__.split(".")[0]}_{cls.__name__.lower()}'
            cursor.execute(f'TRUNCATE TABLE "{name_table}" RESTART IDENTITY CASCADE')
            print(colorama.Fore.GREEN + f'Таблица "{name_table}" очищена!' \
                  + colorama.Fore.RESET)


class Category(models.Model, Truncate):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model, Truncate):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(default=0, verbose_name='Цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, **NULLABLE, verbose_name='Дата последнего изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название верси')
    flag_current_version = models.BooleanField(**NULLABLE, default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.version_number} {self.flag_current_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Contacts(models.Model, Truncate):
    country = models.CharField(max_length=100, verbose_name='Страна')
    inn = models.TextField(default=None, verbose_name='ИНН', **NULLABLE)
    address = models.TextField(verbose_name='Адресс')
    phone = models.TextField(default=None, verbose_name='Телефон')

    def __str__(self):
        return f'{self.country} {self.address} {self.phone}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
