from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordResetView
from django.forms import TextInput

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(UserCreationForm, StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm, StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class RecoverPasswordForm(PasswordResetView, StyleFormMixin):
    class Meta:
        model = User
        fields = ('email')
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Укажите почту при регистрации'}),
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get('email')
    #
    #     if email:
    #         valid_email = User.objects.filter(email=email)
    #
    #         if not valid_email.exists():
    #             raise forms.ValidationError("Пользователь с такой почтой не зарегестрирован")
    #
    #     return cleaned_data
