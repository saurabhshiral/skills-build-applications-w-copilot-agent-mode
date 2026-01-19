from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        self.user1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

    def test_user_team(self):
        self.assertEqual(self.user1.team.name, 'Marvel')
        self.assertEqual(self.user2.team.name, 'DC')

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user1, type='Running', duration=30, calories=300, date='2024-01-01')
        self.assertEqual(activity.user.name, 'Spider-Man')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Cardio Blast', description='High intensity', suggested_for='Marvel')
        self.assertEqual(workout.suggested_for, 'Marvel')

    def test_leaderboard_creation(self):
        marvel = Team.objects.get(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=marvel, points=1000)
        self.assertEqual(leaderboard.team.name, 'Marvel')
