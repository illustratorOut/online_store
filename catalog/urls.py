from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, ContactsListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('product-<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('contacts', ContactsListView.as_view(), name='contacts'),

]
