from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from octofit_tracker.models import CustomUser, Team, Activity, Leaderboard, Workout
        # Delete all data
        CustomUser.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            CustomUser.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel),
            CustomUser.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel),
            CustomUser.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc),
            CustomUser.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', first_name='Diana', last_name='Prince', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='Run', duration=30, calories=300),
            Activity.objects.create(user=users[1], type='Swim', duration=45, calories=400),
            Activity.objects.create(user=users[2], type='Bike', duration=60, calories=500),
            Activity.objects.create(user=users[3], type='Yoga', duration=50, calories=200),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength workout for superheroes'),
            Workout.objects.create(name='Agility Training', description='Agility and speed workout'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=1000)
        Leaderboard.objects.create(user=users[1], score=900)
        Leaderboard.objects.create(user=users[2], score=950)
        Leaderboard.objects.create(user=users[3], score=920)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))

    def get_or_create_team_model(self):
        from django.apps import apps
        try:
            return apps.get_model('octofit_tracker', 'Team')
        except LookupError:
            class Team(models.Model):
                name = models.CharField(max_length=100, unique=True)
                class Meta:
                    app_label = 'octofit_tracker'
            return Team

    def get_or_create_activity_model(self):
        from django.apps import apps
        try:
            return apps.get_model('octofit_tracker', 'Activity')
        except LookupError:
            class Activity(models.Model):
                user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
                type = models.CharField(max_length=50)
                duration = models.IntegerField()
                calories = models.IntegerField()
                class Meta:
                    app_label = 'octofit_tracker'
            return Activity

    def get_or_create_leaderboard_model(self):
        from django.apps import apps
        try:
            return apps.get_model('octofit_tracker', 'Leaderboard')
        except LookupError:
            class Leaderboard(models.Model):
                user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
                score = models.IntegerField()
                class Meta:
                    app_label = 'octofit_tracker'
            return Leaderboard

    def get_or_create_workout_model(self):
        from django.apps import apps
        try:
            return apps.get_model('octofit_tracker', 'Workout')
        except LookupError:
            class Workout(models.Model):
                name = models.CharField(max_length=100)
                description = models.TextField()
                class Meta:
                    app_label = 'octofit_tracker'
            return Workout
