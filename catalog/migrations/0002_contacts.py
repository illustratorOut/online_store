# Generated by Django 4.2.7 on 2023-11-13 19:29

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('inn', models.TextField(blank=True, default=None, null=True, verbose_name='ИНН')),
                ('address', models.TextField(verbose_name='Адресс')),
                ('phone', models.TextField(default=None, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
            bases=(models.Model, catalog.models.Truncate),
        ),
    ]
