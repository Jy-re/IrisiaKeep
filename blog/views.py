from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Character, Lore, Book
from django.shortcuts import render, get_object_or_404


def home(request):
  characters = Character.objects.all()
  return render(request, 'main.html', {'characters': characters})

def post(request):
  template = loader.get_template('posts.html')
  return HttpResponse(template.render())

def wprojects(request):
  books = Book.objects.all()
  print(books)
  characters = Character.objects.all()
  lores = Lore.objects.all()
  return render(request, 'writing_projects.html', {'books':books, 'characters': characters, 'lores': lores, })

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

def create_lore(request):
   if request.method == 'POST':
      worldname = request.POST.get('worldname')
      overview = request.POST.get('overview')
      geography = request.POST.get('geography')
      culturesociety = request.POST.get('culturesociety')
      history = request.POST.get('history')
      magictech = request.POST.get('magictech')
      politics = request.POST.get('politics')
      economy = request.POST.get('economy')
      creatures = request.POST.get('creatures')
      language = request.POST.get('language')
      arts = request.POST.get('arts')
      miscellaneous = request.POST.get('miscellaneous')

      lore = Lore.objects.create(worldname=worldname, overview=overview, geography=geography,culturesociety=culturesociety, history=history, magictech=magictech, politics=politics, economy=economy, creatures=creatures, language=language, arts=arts, miscellaneous=miscellaneous)
      lores = Lore.objects.all()
      print(lores)

      return render(request, 'main.html', {'lores': lores})
   
   return render(request, 'lore_form.html')

def lore_detail(request, lore_id):
    lore = get_object_or_404(Lore, pk=lore_id)
    return render(request, 'lore_details.html', {'lore': lore})

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        plot = request.POST.get('plot')
        author = request.POST.get('author')
        datestart = request.POST.get('datestart')
        lore = request.POST.get('lore')
        characters = request.POST.getlist('characters')  # Use getlist() to get multiple selected values

        characters = [get_object_or_404(Character, pk=char_id) for char_id in characters]
        lore = get_object_or_404(Lore, pk=lore)

        book = Book.objects.create(title=title, plot=plot, author=author, datestart=datestart, lore=lore)
        book.characters.set(characters)  # Use the set() method to set the many-to-many relationship
        book.save()

        books = Book.objects.all()
        print(books)

        return render(request, 'main.html', {'books': books})

    characters = Character.objects.all()
    lores = Lore.objects.all()
    return render(request, 'book_form.html', {'characters': characters, 'lores': lores})
  
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})
