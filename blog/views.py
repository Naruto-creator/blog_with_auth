from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'  # This is the fields for form of new post
    # and If you want to create new post You have to fill all fields


class BlogUpdateView(UpdateView):
    madel = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text', ]

    def get_queryset(self):
        return Post.objects.all()


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')






