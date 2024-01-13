import random

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from users.forms import UserRegisterForm, UserProfileForm, RecoverPasswordForm
from users.models import User
from users.services import get_send_mail


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
                    try:
                        get_send_mail(self.object.email, random_key_registration)
                        new_key.registration_key = random_key_registration
                        new_key.save()
                    except:
                        pass

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
