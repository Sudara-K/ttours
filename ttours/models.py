from django.db import models

class Season(models.Model):
    start_date=models.DateTimeField('Season start date')
    end_date=models.DateTimeField('Season end date')
    name=models.CharField(max_length=200)
    last_modified=models.DateTimeField()

class Player(models.Model):
    player_name=models.CharField(max_length=25)
    created_date=models.DateTimeField('Date Joined')
    pic_path=models.CharField(max_length=300)
    last_modified=models.DateTimeField()

class Season_Players(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    season=models.ForeignKey(Season,on_delete=models.CASCADE)
    rating=models.IntegerField(default=2000)
    last_modified=models.DateTimeField()

class Match(models.Model):
    match_time=models.DateTimeField()
    player1=models.ForeignKey(Season_Players,on_delete=models.CASCADE,related_name='player1')
    player2=models.ForeignKey(Season_Players,on_delete=models.CASCADE,related_name='player2')
    player1_score=models.IntegerField(default=0)
    player2_score=models.IntegerField(default=0)
    last_modified=models.DateTimeField()


# Create your models here.
