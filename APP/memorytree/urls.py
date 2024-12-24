from django.urls import path
from . import views

app_name = 'memorytree'
urlpatterns = [
    path(r'', views.index, name='index'),
]