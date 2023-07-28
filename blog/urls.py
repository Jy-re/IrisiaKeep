from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.create_character, name='home'), 
    path('posts/', views.post, name='blog'),
    path('create-post/', views.create, name='create-post'),
    path('create-character/', views.create_character, name='create-character'),
    path('character/<int:character_id>/', views.character_detail, name='character-detail'),
]