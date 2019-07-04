from django.views.generic import ListView, TemplateView
from .models import Stanowisko, Samochod


class Stanowsiko(ListView):
    model = Post
    template_name = 'post/home.html'

class Stanowisko_1(ListView):
    model = Samochod
    template_name = 'post/stanowisko_1.html'

class Stanowisko_2(ListView):
    model = Samochod
    template_name = 'post/stanowisko_2.html'

