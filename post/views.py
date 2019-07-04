from django.views.generic import ListView, TemplateView
from .models import Post


class PostsPage(ListView):
    model = Post
    template_name = 'post/home.html'

class Stanowisko_1(TemplateView):
    template_name = 'post/stanowisko_1.html'

class Stanowisko_2(TemplateView):
    template_name = 'post/stanowisko_2.html'

