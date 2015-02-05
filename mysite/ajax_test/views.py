from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
  template = loader.get_template('index.html')
  context = RequestContext(request)
  return HttpResponse(template.render(context))

def async(request):
  class Message(object):
    def __init__(self, text):
      self.text = text
    def __str__(self):
      return str(self.text)
    def __repr__(self):
      return 'Message(' + self.text + ')'
  received = request.GET['msg']
  return HttpResponse(Message('Response from the server at /ajax_test/async: you sent "' + received + '"'))
