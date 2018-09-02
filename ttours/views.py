from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Player,Season,Season_Players,Match

class IndexView(generic.ListView):
    template_name='ttours/index.html'
    context_object_name='seasons'
    def get_queryset(self):
        return Season.objects.all().order_by('-start_date')

class SeasonView(generic.DetailView):
    template_name='ttours/season.html'
    model=Season

class PlayerView(generic.ListView):
    template_name='ttours/players.html'
    context_object_name='players'
    def get_queryset(self):
        return Season.objects.all()




# Create your views here.
