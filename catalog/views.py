from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contacts


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsListView(ListView):
    model = Contacts
