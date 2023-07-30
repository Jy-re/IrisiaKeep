from django import forms
from .models import Character, Lore, Book, Post

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'age', 'personality', 'background', 'goals', 'strengths', 'weakness', 'skills', 'hobbies', 'backstory', 'image']
        

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['worldname','overview', 'geography', 'culturesociety', 'history', 'magictech', 'politics', 'economy', 'creatures', 'language', 'arts', 'miscellaneous', 'image']

class BookForm(forms.ModelForm):
    characters = forms.ModelMultipleChoiceField(
        queryset=Character.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Book
        fields = ['title', 'plot', 'author', 'datestart', 'lore', 'characters', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model: Post
        fields = ['title', 'content', 'image']