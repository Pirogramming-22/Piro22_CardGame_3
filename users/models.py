from django.db import models

# Create your models here.
class User(models.Model):
  user=models.CharField(max_length=50,unique=True)
<<<<<<< HEAD
  score=models.IntegerField(default=0)
=======
  score=models.IntegerField(default=0)

  def __str__(self):
    return self.user
>>>>>>> e7aef9b5c38ff81117ad1a2371696249a9280604
