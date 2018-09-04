from django.forms import ModelForm,Textarea
from .models import Match


# Create the form class.
class MatchForm(ModelForm):
    def __init__(self, *args,**kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Match
        fields=['player1','player2','player1_score','player2_score']

