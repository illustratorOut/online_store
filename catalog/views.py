from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def catalog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}\nphone: {phone}\nmessage: {message}')

    return render(request, 'catalog/catalog.html')
