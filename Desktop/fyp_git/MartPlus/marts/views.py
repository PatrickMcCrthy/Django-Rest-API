from django.http import HttpResponse
from django.template import loader

def marts(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def skibbereen(request):
  template = loader.get_template('martscreens/skibbereen.html')
  return HttpResponse(template.render())


