from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import show
# Create your views here.
def index(request):
    return render(request, 'index.html')

def database(request):
    template = loader.get_template('database.html')
    return HttpResponse(template.render({},request))

def add1(request):
    template = loader.get_template('add1.html')
    return HttpResponse(template.render({},request))

def addshow(request):
    show_id = request.POST['show_id']
    name = request.POST['name']
    season = request.POST['season']
    episode = request.POST['episodes']
    Show = show(show_id=show_id,name=name,season=season,episodes=episode)
    Show.save() 
    return HttpResponseRedirect(reverse('database'))

def displayshow(request):
    Show = show.objects.all().values()
    context = {
        'Show':Show
    }
    template = loader.get_template('displayshow.html')
    return HttpResponse(template.render(context,request))
