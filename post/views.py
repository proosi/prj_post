from django.views.generic import ListView
from .models import Post


class PostsPage(ListView):
    model = Post
    template_name = 'post/home.html'

    
