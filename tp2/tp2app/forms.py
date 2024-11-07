from django import forms
from tp2app.models import Author, Book, Category

# Formulaire pour l'ajout et la modification d'un auteur
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']

# Formulaire pour l'ajout et la modification d'un livre
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']

# Formulaire pour l'ajout et la modification d'une catégorie
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
