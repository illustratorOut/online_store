from django.db import models

NULLABLE = {
    'null': 'True',
    'blank': 'True',
}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(**NULLABLE, max_length=150, verbose_name='slug')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение')
    date_create = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    count_views = models.IntegerField(**NULLABLE, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} {self.date_create}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
