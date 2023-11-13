from django.shortcuts import render

from catalog.models import Product, Contacts


def home(request):
    news = Product.objects.all().order_by('-id')[:5]
    return render(request, 'catalog/home.html', {'news': news})


def catalog(request):
    info_contacts = Contacts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}\nphone: {phone}\nmessage: {message}')

    return render(request, 'catalog/catalog.html', {'info_contacts': info_contacts})
