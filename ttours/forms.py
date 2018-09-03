from django.forms import ModelForm
from .models import Match

# Create the form class.
class MatchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.initial['season'] = kwargs.pop('season' , None)
    class Meta:
        model = Match
        fields=['match_time','player1','player2','season','player1_score','player2_score']
