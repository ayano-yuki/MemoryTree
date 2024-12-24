from django.contrib import admin
from django.urls import path, include # includeを追記

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('memorytree.urls')), # ここを追記
]