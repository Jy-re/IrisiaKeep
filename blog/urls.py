from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.blog, name='blog'),
]