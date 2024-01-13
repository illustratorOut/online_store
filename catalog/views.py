from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Version, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.services import get_cached_subjects_for_product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс создания товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, ListView):
    """Класс отображения товара"""
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk

        return context_data


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.object.owner != self.request.user:
            product_fields = [f for f in form.fields.keys()]
            for field in product_fields:
                if not self.request.user.has_perm(f'catalog.set_{field}'):
                    del form.fields[field]
        return form

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Валидация формы редактирование товара и Version"""

        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """Класс удаления товара"""
    model = Product
    success_url = reverse_lazy('catalog:category')


class ProductDetailView(DetailView):
    """Класс для вывода статических страниц с информацией"""
    model = Product

    def get_context_data(self, **kwargs):
        """Реализация функции кеширования"""
        context_data = super().get_context_data(**kwargs)
        context_data['subjects'] = get_cached_subjects_for_product(self.object.pk)
        return context_data


class CategoryListView(LoginRequiredMixin, ListView):
    """Класс отображения категории"""
    model = Category


class ContactsListView(ListView):
    """Класс отображения контактов"""
    model = Contacts
