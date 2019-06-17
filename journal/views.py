from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body', 'author']