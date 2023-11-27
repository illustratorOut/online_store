from django.shortcuts import render

from catalog.models import Product, Contacts
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsListView(ListView):
    model = Contacts


def home(request):
    news = Product.objects.all().order_by('-id')[:5]
    context = {
        'title': 'Главная',
        'news': news,
    }
    return render(request, 'catalog/home.html', context)


def catalog(request):
    info_contacts = Contacts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}\nphone: {phone}\nmessage: {message}')

    context = {
        'title': 'Контакты',
        'info_contacts': info_contacts,
    }
    return render(request, 'catalog/catalog.html', context)


def product(request, pk):
    info_product = Product.objects.filter(pk=pk)
    context = {
        'info_product': info_product,
    }

    return render(request, 'catalog/product.html', context)
