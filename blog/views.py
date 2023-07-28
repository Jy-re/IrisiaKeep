from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import CharacterForm
from .models import Character
from django.shortcuts import render, get_object_or_404


def home(request):
  characters = Character.objects.all()
  return render(request, 'main.html', {'characters': characters})

def post(request):
  template = loader.get_template('posts.html')
  return HttpResponse(template.render())

def create(request):
  template = loader.get_template('create_post.html')
  return HttpResponse(template.render())


def create_character(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      age = request.POST.get('age')
      personality = request.POST.get('personality')
      background = request.POST.get('background')
      goals = request.POST.get('goals')
      strengths = request.POST.get('strengths')
      weakness = request.POST.get('weakness')
      skills = request.POST.get('skills')
      hobbies = request.POST.get('hobbies')
      backstory = request.POST.get('backstory')

      character = Character.objects.create(name=name, age=age, personality=personality,background=background, goals=goals, strengths=strengths, weakness=weakness, skills=skills, hobbies=hobbies, backstory=backstory)
      characters = Character.objects.all()
      print(characters)

      return render(request, 'main.html', {'characters': characters})
   
   return render(request, 'character_form.html')

def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character_details.html', {'character': character})