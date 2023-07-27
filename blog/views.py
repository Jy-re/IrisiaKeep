from django.http import HttpResponse
from django.template import loader

def blog(request):
  template = loader.get_template('posts.html')
  return HttpResponse(template.render())