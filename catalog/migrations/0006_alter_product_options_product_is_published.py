# Generated by Django 4.2.7 on 2024-01-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_version_owner_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_is_published', 'Может публиковать товары'), ('set_category', 'Может изменять категорию товара'), ('set_description', 'Может изменять описание товара')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Признак публикации'),
        ),
    ]