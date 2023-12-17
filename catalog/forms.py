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
        exclude = ('owner',)

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
        exclude = ('owner',)

    def clean(self):
        cleaned_data = super().clean()
        flag_current_version = cleaned_data.get('flag_current_version')
        product = cleaned_data.get('product')
        print(product)

        if flag_current_version:
            existing_active_versions = Version.objects.filter(
                product=product,
                flag_current_version=True
            ).exclude(pk=self.instance.pk)  # Исключает по ID

            # Возвращает True, если возвращаемый QuerySet содержит один или несколько объектов, и значение False, если QuerySet пустой.
            if existing_active_versions.exists():
                raise forms.ValidationError('Одновременно для продукта может быть только одна активная версия')

        return cleaned_data
