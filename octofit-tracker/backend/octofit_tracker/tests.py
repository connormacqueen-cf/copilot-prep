from django.test import TestCase
from .models import CustomUser, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.team, team)

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=10, calories=100)
        self.assertEqual(activity.user, user)

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=123)
        self.assertEqual(leaderboard.user, user)

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')
