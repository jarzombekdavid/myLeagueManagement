from django.db import models

# Create your models here.

class Season(models.Model):
	name = models.CharField(max_length-200)
	draft_time = models.DateTimeField()
	
class Team(models.Model):
	name = models.CharField(max_length-200)
	season = models.ForeignKey(Season, unique=True)
	user_1 = models.ForeignKey(User, unique=True)
	user_2 = models.ForeignKey(User, unique=True)
	multi_user = 	models.BooleanField()
	APG = models.DecimalField()
	RPG = models.DecimalField()
	PPG = models.DecimalField()
	SPF = models.DecimalField()
	FG% = models.DecimalField()
	
class Game(models.Model):
	season = models.ForeignKey(Season, unique=True)
	home_team = models.ForeignKey(Team, unique=True)
	awawy_team = models.ForeignKey(Team, unique=True)
	score_home = models.IntegerField()
	score_away = models.IntegerField()
	winner = models.ForeignKey(Team, unique=True)
	
class LeaderboardPlayer(models.Model):
	season = models.ForeignKey(Season, unique=True)
	name = models.CharField(max_length-200)
	category = models.CharField(max_length-200)
	APG = models.DecimalField()
	RPG = models.DecimalField()
	PPG = models.DecimalField()
	SPF = models.DecimalField()
	FG% = models.DecimalField()
	
class MockDraftPick(models.Model):
	season = models.ForeignKey(Season, unique=True)
	round = models.IntegerField()
	team = models.ForeignKey(Team, unique=True)
	player_name = models.CharField(max_length-200)
	
class DraftPick(models.Model):
	season = models.ForeignKey(Season, unique=True)
	round = models.IntegerField()
	team = models.ForeignKey(Team, unique=True)
	player_name = models.CharField(max_length-200)
	
class Roster(models.Model):
	season = models.ForeignKey(Season, unique=True)
	team = models.ForeignKey(Team, unique=True)
	player_name = models.CharField(max_length-200)
