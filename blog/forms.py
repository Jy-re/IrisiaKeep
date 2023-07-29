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
    class Meta:
        model: Book
        fields = ['plot', 'author', 'date_started', 'date_ended', 'image']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['world_name'].queryset = Lore.objects.all()
        self.fields['name'].queryset = Character.objects.all()

class PostForm(forms.ModelForm):
    class Meta:
        model: Post
        fields = ['title', 'content', 'image']