from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, catalog, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts', catalog, name='contacts'),
    path('product-<int:pk>/', product, name='product'),
]
