from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import show, user_progress
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

def wishlist(request):
    template = loader.get_template('wishlist.html')
    shows = user_progress.objects.all().values()
    context = {
        "shows":shows,
    }
    return HttpResponse(template.render(context,request))

def addtowishlist(request):
    # print('Hi')
    #This should add that movie to the wish list
    #render same template
    
    cshow = request.POST['title']
    print(cshow)
    cshows = show.objects.get(name = cshow, season = 1)
    # print(type(cshows))
    # print(cshows)
    new_show = user_progress(show_name=cshows.name,season=1,episodes = 1)
    new_show.save()
    return HttpResponseRedirect(reverse('index'))

