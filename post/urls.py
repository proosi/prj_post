from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsPage.as_view() , name='home'),
]