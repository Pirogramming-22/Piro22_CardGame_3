from django.db import models
from users.models import CustomUser

# Create your models here.
class Game(models.Model):
  attacker = models.ForeignKey(CustomUser, related_name='attacker', on_delete=models.CASCADE)
  defender = models.ForeignKey(CustomUser, related_name='defender', on_delete=models.CASCADE)
  attacker_card = models.IntegerField()
  defender_card = models.IntegerField(null=True, blank=True)
  result = models.CharField(max_length=10, null=True, blank=True)
  winner = models.ForeignKey(CustomUser, related_name='winner', null=True, blank=True, on_delete=models.SET_NULL)
  is_greater_wins = models.BooleanField()