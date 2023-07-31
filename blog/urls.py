from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-posts/', views.create_post, name='blog'),
    path('writing-projects/', views.wprojects, name='writing-projects'),
    path('create-post/', views.create_post, name='create-post'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('create-character/', views.create_character, name='create-character'),
    path('character/<int:character_id>/', views.character_detail, name='character-detail'),
    path('create-lore/', views.create_lore, name='create-lore'),
    path('lore/<int:lore_id>/', views.lore_detail, name='lore-detail'),
    path('create-book/', views.create_book, name='create-book'),
    path('book/<int:book_id>/', views.book_detail, name='book-detail'),
]
