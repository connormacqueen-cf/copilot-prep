from django.contrib.auth.models import AbstractUser
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

class Activity(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Leaderboard(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user.username}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
