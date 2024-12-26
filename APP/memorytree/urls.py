from django.urls import path
from . import views

app_name = 'memorytree'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'write_diary/',  views.write_diary, name='write_diary'),
    path(r'see_word_cloud/', views.see_word_cloud, name='see_word_cloud'),
    path(r'diary_success/', views.diary_success, name='diary_success'),
]