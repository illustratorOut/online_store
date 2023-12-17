import os
import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from users.forms import UserRegisterForm, UserProfileForm, RecoverPasswordForm
from users.models import User


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        while True:
            random_key_registration = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            if form.is_valid():
                if User.objects.filter(registration_key=random_key_registration):
                    continue
                else:
                    new_key = form.save()
                    new_key.registration_key = random_key_registration
                    new_key.save()
                    send_mail(
                        subject=f'Активация акаунта',
                        message=f'Для завершения регистрации перейдите по сыллке http://127.0.0.1:8000/users/key-registration/{random_key_registration}',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[self.object.email])
                    return super().form_valid(form)
        return super().form_valid(form)


class ProfileView(UpdateView):
    """Профиль пользователя"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE
    }

    def get_object(self, queryset=None):
        return self.request.user


class RecoverPassword(ListView):
    """Востановление пароля по email"""
    model = User
    form_class = RecoverPasswordForm


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject=f'Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email])
    request.user.set_password(new_password)
    request.user.save()
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
