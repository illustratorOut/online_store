from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify
import os
from blog.models import Blog

from django.core.mail import send_mail


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'is_published')
    success_url = reverse_lazy('blog:home')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:home')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        if self.object.count_views == 10:
            send_mail(
                subject=f'Сайт',
                message=f'Ура карточка с товаром "{self.object.title}" http://127.0.0.1:8000{self.request.get_full_path()} достигла 100 просмотров!!!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[os.getenv('MAIL_SENDING')])

        return self.object
