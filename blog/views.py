from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def post(request):
  template = loader.get_template('posts.html')
  return HttpResponse(template.render())

def create(request):
  template = loader.get_template('create_post.html')
  return HttpResponse(template.render())