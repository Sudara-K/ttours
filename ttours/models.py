from django.db import models
import datetime
from django.utils import timezone

class Season(models.Model):
    start_date=models.DateTimeField('Season start date')
    end_date=models.DateTimeField('Season end date')
    name=models.CharField(max_length=200)
    last_modified=models.DateTimeField(default=timezone.now)
    def is_current_season(self):
        now=timezone.now()
        return self.start_date<=now<=self.end_date
    def __str__(self):
       return self.name

class Player(models.Model):
    player_name=models.CharField(max_length=25)
    created_date=models.DateTimeField('Date Joined')
    pic_path=models.CharField(max_length=300)
    last_modified=models.DateTimeField(default=timezone.now)
    def __str__(self):
       return self.player_name

class Season_Players(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    season=models.ForeignKey(Season,on_delete=models.CASCADE)
    rating=models.IntegerField(default=2000)
    last_match=models.DateTimeField(default=timezone.now)
    wins=models.IntegerField(default=0)
    losses=models.IntegerField(default=0)
    win_percentage=models.IntegerField(default=0)
    last_modified=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=['-rating']
    def getPlayerName(self):
        return self.player.player_name
    def __str__(self):
       return self.player.player_name + '('+self.season.name+')'

class Match(models.Model):
    match_time=models.DateTimeField(default=timezone.now)
    player1=models.ForeignKey(Season_Players,on_delete=models.CASCADE,related_name='player1')
    player2=models.ForeignKey(Season_Players,on_delete=models.CASCADE,related_name='player2')
    season=models.ForeignKey(Season,on_delete=models.CASCADE,default=1)
    player1_score=models.IntegerField(default=0)
    player2_score=models.IntegerField(default=0)
    player1_rating_delta=models.IntegerField(default=0)
    player2_rating_delta=models.IntegerField(default=0)
    winner=models.ForeignKey(Season_Players,on_delete=models.CASCADE,related_name='winner')
    last_modified=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=['-match_time']
    def __str__(self):
       return self.player1.player.player_name+' vs '+self.player2.player.player_name + ' ['+self.season.name+']' +' ('+"{:%B %d, %Y}".format(self.match_time)+')'


# Create your models here.
