from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(str(self.user), 'testuser')


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
        self.assertTrue(isinstance(self.team, Team))
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='507f1f77bcf86cd799439011',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.distance, 5.0)
        self.assertTrue(isinstance(self.activity, Activity))


class APIEndpointsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='apiuser',
            email='api@example.com',
            password='apipass123'
        )
        self.team = Team.objects.create(
            name='API Team',
            description='An API test team'
        )
    
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
    
    def test_users_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_teams_list(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_activities_list(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_list(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_workouts_list(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='viewsetuser',
            email='viewset@example.com',
            password='viewsetpass123'
        )
    
    def test_create_user(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(reverse('user-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_user(self):
        response = self.client.get(
            reverse('user-detail', kwargs={'pk': str(self.user._id)})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'viewsetuser')


class TeamViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name='ViewSet Team',
            description='A viewset test team'
        )
    
    def test_create_team(self):
        data = {
            'name': 'New Team',
            'description': 'A new test team'
        }
        response = self.client.post(reverse('team-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_team(self):
        response = self.client.get(
            reverse('team-detail', kwargs={'pk': str(self.team._id)})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'ViewSet Team')
