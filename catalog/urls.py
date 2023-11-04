from django.urls import path

from catalog.views import home, catalog

urlpatterns = [
    path('', home),
    path('contacts', catalog),
]
