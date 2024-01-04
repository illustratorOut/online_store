from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('1234S5678')
        user.save()

        user2 = User.objects.create(
            email='user@sky.pro',
            first_name='User',
            last_name='Users',
            is_active=True,
        )
        user2.set_password('1234S5678')
        user2.save()
