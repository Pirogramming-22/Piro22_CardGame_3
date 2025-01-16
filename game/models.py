from django.db import models
from users.models import User
from users.models import User

# Create your models here.
class Game(models.Model):
  attacker = models.ForeignKey(User, related_name='attacker', on_delete=models.CASCADE)
  defender = models.ForeignKey(User, related_name='defender', on_delete=models.CASCADE)
  attacker_card = models.IntegerField()
  defender_card = models.IntegerField(null=True, blank=True)
  result = models.CharField(max_length=10, null=True, blank=True)
  winner = models.ForeignKey(User, related_name='winner', null=True, blank=True, on_delete=models.SET_NULL)
  is_greater_wins = models.BooleanField()