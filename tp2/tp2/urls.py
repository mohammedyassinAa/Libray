from django.contrib import admin
from django.urls import path
from tp2app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Route pour l'administration Django
    path('author/create/', views.author_create, name='author_create'),  # Création d'un auteur
    path('author/', views.author_list, name='author_list'),  # Liste des auteurs
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),  # Détails d'un auteur
    path('book/', views.book_list, name='book_list'),  # Liste des livres
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Détails d'un livre
    path('category/', views.category_list, name='category_list'),  # Liste des catégories
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),  # Détails d'une catégorie
]
