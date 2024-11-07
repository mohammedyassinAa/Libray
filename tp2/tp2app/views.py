from django.shortcuts import render, redirect
from tp2app.models import Author, Book, Category
from tp2app.forms import AuthorForm, BookForm, CategoryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Vue pour afficher tous les auteurs
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'tp2app/author_list.html', {'authors': authors})

# Vue pour afficher tous les livres
def book_list(request):
    books = Book.objects.all()
    return render(request, 'tp2app/book_list.html', {'books': books})

# Vue pour afficher toutes les catégories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'tp2app/category_list.html', {'categories': categories})

# Vue pour afficher les détails d'un auteur
def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'tp2app/author_detail.html', {'author': author, 'books': books})

# Vue pour afficher les détails d'un livre
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    categories = book.categories.all()
    return render(request, 'tp2app/book_detail.html', {'book': book, 'categories': categories})

# Vue pour afficher les détails d'une catégorie
def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    books = category.books.all()
    return render(request, 'tp2app/category_detail.html', {'category': category, 'books': books})

# Vue pour créer un auteur
def author_create(request):
    if request.method == 'POST':  # Si le formulaire est soumis
        form = AuthorForm(request.POST)
        if form.is_valid():  # Si le formulaire est valide
            form.save()  # Sauvegarde de l'auteur dans la base de données
            return HttpResponseRedirect(reverse('author_list'))  # Rediriger vers la liste des auteurs
    else:
        form = AuthorForm()  # Créer un formulaire vide si la requête est GET

    return render(request, 'tp2app/author_form.html', {'form': form})  # Affichage du formulaire
