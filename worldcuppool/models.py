from django.db import models

# Create your models here.
class Team(models.Model):
	teamID=models.AutoField(primary_key=True)
	name = models.CharField(max_length=254)
	advanced = models.BooleanField(default=False)
	knockout_wins = models.IntegerField()

	def __unicode__(self):
		return self.name

class User(models.Model):
	userID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=254)
	email = models.CharField(max_length=254)
	pick1 = models.ForeignKey(Team, related_name='user_pick_1', default=0)
	pick2 = models.ForeignKey(Team, related_name='user_pick_2', default=0)
	pick3 = models.ForeignKey(Team, related_name='user_pick_3', default=0)
	pick4 = models.ForeignKey(Team, related_name='user_pick_4', default=0)
	pick5 = models.ForeignKey(Team, related_name='user_pick_5', default=0)
	pick6 = models.ForeignKey(Team, related_name='user_pick_6', default=0)
	pick7 = models.ForeignKey(Team, related_name='user_pick_7', default=0)
	pick8 = models.ForeignKey(Team, related_name='user_pick_8', default=0)
	pick9 = models.ForeignKey(Team, related_name='user_pick_9', default=0)
	pick10 = models.ForeignKey(Team, related_name='user_pick_10', default=0)
	pick11 = models.ForeignKey(Team, related_name='user_pick_11', default=0)
	pick12 = models.ForeignKey(Team, related_name='user_pick_12', default=0)
	pick13 = models.ForeignKey(Team, related_name='user_pick_13', default=0)
	pick14 = models.ForeignKey(Team, related_name='user_pick_14', default=0)
	pick15 = models.ForeignKey(Team, related_name='user_pick_15', default=0)
	pick16 = models.ForeignKey(Team, related_name='user_pick_16', default=0)

	def __unicode__(self):
		return self.name

