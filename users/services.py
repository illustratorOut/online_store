import random
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import User


def get_send_mail(mail, random_key_registration):
    """Отправка ссылки аунтификации на почту"""

    url = 'http://127.0.0.1:8000'
    send_mail(
        subject=f'Активация акаунта',
        message=f'Для завершения регистрации перейдите по сыллке {url}/users/key-registration/{random_key_registration}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[mail],
    )


def generate_new_password(request):
    """Генерация нового пароля и отправка на почту"""

    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    try:
        send_mail(
            subject=f'Вы сменили пароль',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
        )

        request.user.set_password(new_password)
        request.user.save()
    except:
        return render(request, 'users/error_404.html')

    return redirect(reverse('catalog:list'))


def is_active_key_registration(request, key):
    users = User.objects.filter(registration_key=key)
    if users:
        user = users[0]
        user.is_active = True
        user.save()
    else:
        return redirect(reverse('users:login'))

    return render(request, 'users/success_registration.html')
