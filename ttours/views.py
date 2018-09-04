from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from.forms import MatchForm
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
    def get_success_url(self, **kwargs):
        return reverse_lazy('ttours:season', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form,**kwargs):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        match=form.save(commit=False)
        player1=form.cleaned_data['player1']
        player2=form.cleaned_data['player2']
        player1_score=form.cleaned_data['player1_score']
        player2_score=form.cleaned_data['player2_score']
        match.season=Season.objects.get(id=self.kwargs['pk'])
        match.match_time=timezone.now()
        percent=1 / (1 + 10 ** ((player2.rating - player1.rating) / 400))
        win=round((1-percent)*50)
        loss=round((0-percent)*50)

        if(player1_score>player2_score):
            match.player1_rating_delta=win
            match.player2_rating_delta=-win
            player1.rating+=win
            player2.rating-=win
            player1.wins+=1
            player2.losses+=1
            match.winner=player1
        else:
            match.player1_rating_delta=loss
            match.player2_rating_delta=-loss
            player1.rating+=loss
            player2.rating-=loss
            player1.losses+=1
            player2.wins+=1
            match.winner=player2
        player1.last_match=timezone.now()
        player2.last_match=timezone.now()
        player1totgames=player1.wins+player1.losses
        player2totgames=player2.wins+player2.losses
        if(player1.wins>0):
            player1.win_percentage=round((player1.wins/player1totgames)*100,2)
        if(player2.wins>0):
            player2.win_percentage=round((player2.wins/player2totgames)*100,2)
        player2.save()
        player1.save()
        form.save()
        return super().form_valid(form)

class PlayerView(generic.ListView):
    template_name='ttours/players.html'
    context_object_name='players'
    def get_queryset(self):
        return Season.objects.all()




# Create your views here.
