from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from .forms import MatchForm

from .models import Player,Season,Season_Players,Match

class IndexView(generic.ListView):
    template_name='ttours/index.html'
    context_object_name='seasons'
    def get_queryset(self):
        return Season.objects.all().order_by('-start_date')

class SeasonView(generic.DetailView):
    template_name='ttours/season.html'
    model=Season
    def get_context_data(self, **kwargs):
         context = super(SeasonView, self).get_context_data(**kwargs)
         context['matches'] = Match.objects.filter(season_id=self.object.id)[:10]
         return context

class MatchView(generic.FormView):
    template_name='ttours/addmatch.html'
    form_class=MatchForm
    success_url=reverse_lazy('ttours:season')
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

class PlayerView(generic.ListView):
    template_name='ttours/players.html'
    context_object_name='players'
    def get_queryset(self):
        return Season.objects.all()




# Create your views here.
