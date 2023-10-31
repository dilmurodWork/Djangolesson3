# 5 create urls.py in your application

from django.urls import path
from .views import index_view

urlpatterns = [
    path('', index_view, name='home')  # 9
]