from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        self.all_forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                              'радар']

        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        clean_data = self.cleaned_data['name']

        if clean_data in self.all_forbidden:
            raise forms.ValidationError('Запрещенное слово! Измените данные')
        return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data['description']

        if clean_data in self.all_forbidden:
            raise forms.ValidationError('Запрещенное слово! Измените данные')
        return clean_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # здесь реализовать  def clean_name(self): ??
