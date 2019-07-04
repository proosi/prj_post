from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsPage.as_view() , name='home'),
    path('stanowisko_1/', views.Stanowisko_1.as_view() ,name='stanowisko_1'),
    path('stanowisko_2/', views.Stanowisko_2.as_view() ,name='stanowisko_2'),
]