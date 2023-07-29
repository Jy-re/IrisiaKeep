from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.create_character, name='home'), 
    path('posts/', views.post, name='blog'),
    path('writing-projects/', views.wprojects, name='writing-projects'),
    path('create-post/', views.create, name='create-post'),
    path('create-character/', views.create_character, name='create-character'),
    path('character/<int:character_id>/', views.character_detail, name='character-detail'),
    path('create-lore/', views.create_lore, name='create-lore'),
    path('lore/<int:lore_id>/', views.lore_detail, name='lore-detail')
]