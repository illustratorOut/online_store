from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'preview')
    success_url = reverse_lazy('blog:home')


class BlogListView(ListView):
    model = Blog
