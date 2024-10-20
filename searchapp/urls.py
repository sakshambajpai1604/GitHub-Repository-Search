from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_repositories, name='search_repositories'),
]
