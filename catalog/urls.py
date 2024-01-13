from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, ContactsListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='all_product'),
    path('category', cache_page(60)(CategoryListView.as_view()), name='category'),
    path('category/<int:pk>', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),

    # path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    # path('update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='update'),
    # path('delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='delete'),

    path('product-<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('contacts', ContactsListView.as_view(), name='contacts'),

]
