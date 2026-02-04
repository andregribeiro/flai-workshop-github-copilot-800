from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field
        self.stdout.write('Creating unique index on email field...')
        db.users.create_index([('email', 1)], unique=True)

        # Create teams
        self.stdout.write('Creating teams...')
        teams_data = [
            {
                '_id': 'team_marvel',
                'name': 'Team Marvel',
                'description': 'Mightiest Heroes of Earth',
                'created_at': datetime.now()
            },
            {
                '_id': 'team_dc',
                'name': 'Team DC',
                'description': 'Justice League Champions',
                'created_at': datetime.now()
            }
        ]
        db.teams.insert_many(teams_data)

        # Create users (superheroes)
        self.stdout.write('Creating users...')
        users_data = [
            # Team Marvel
            {
                '_id': 'user_ironman',
                'name': 'Tony Stark',
                'email': 'ironman@marvel.com',
                'password': 'hashed_password',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'ironman.jpg',
                    'fitness_level': 'advanced',
                    'goals': 'Build arc reactor-powered endurance'
                }
            },
            {
                '_id': 'user_spiderman',
                'name': 'Peter Parker',
                'email': 'spiderman@marvel.com',
                'password': 'hashed_password',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'spiderman.jpg',
                    'fitness_level': 'advanced',
                    'goals': 'Increase web-slinging agility'
                }
            },
            {
                '_id': 'user_blackwidow',
                'name': 'Natasha Romanoff',
                'email': 'blackwidow@marvel.com',
                'password': 'hashed_password',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'blackwidow.jpg',
                    'fitness_level': 'expert',
                    'goals': 'Maintain spy-level fitness'
                }
            },
            {
                '_id': 'user_hulk',
                'name': 'Bruce Banner',
                'email': 'hulk@marvel.com',
                'password': 'hashed_password',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'hulk.jpg',
                    'fitness_level': 'expert',
                    'goals': 'Control anger through meditation'
                }
            },
            {
                '_id': 'user_thor',
                'name': 'Thor Odinson',
                'email': 'thor@marvel.com',
                'password': 'hashed_password',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'thor.jpg',
                    'fitness_level': 'expert',
                    'goals': 'Worthy of Mjolnir strength training'
                }
            },
            # Team DC
            {
                '_id': 'user_batman',
                'name': 'Bruce Wayne',
                'email': 'batman@dc.com',
                'password': 'hashed_password',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'batman.jpg',
                    'fitness_level': 'expert',
                    'goals': 'Peak human performance'
                }
            },
            {
                '_id': 'user_superman',
                'name': 'Clark Kent',
                'email': 'superman@dc.com',
                'password': 'hashed_password',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'superman.jpg',
                    'fitness_level': 'expert',
                    'goals': 'Maintain Kryptonian strength'
                }
            },
            {
                '_id': 'user_wonderwoman',
                'name': 'Diana Prince',
                'email': 'wonderwoman@dc.com',
                'password': 'hashed_password',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'wonderwoman.jpg',
                    'fitness_level': 'expert',
                    'goals': 'Amazon warrior training'
                }
            },
            {
                '_id': 'user_flash',
                'name': 'Barry Allen',
                'email': 'flash@dc.com',
                'password': 'hashed_password',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'flash.jpg',
                    'fitness_level': 'advanced',
                    'goals': 'Speed force cardio mastery'
                }
            },
            {
                '_id': 'user_aquaman',
                'name': 'Arthur Curry',
                'email': 'aquaman@dc.com',
                'password': 'hashed_password',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'profile': {
                    'avatar': 'aquaman.jpg',
                    'fitness_level': 'advanced',
                    'goals': 'Underwater endurance training'
                }
            }
        ]
        db.users.insert_many(users_data)

        # Create activities
        self.stdout.write('Creating activities...')
        activity_types = ['running', 'cycling', 'swimming', 'weightlifting', 'yoga', 'martial_arts', 'parkour']
        activities_data = []
        
        for user in users_data:
            for i in range(5):
                activity_type = random.choice(activity_types)
                activities_data.append({
                    'user_id': user['_id'],
                    'activity_type': activity_type,
                    'duration': random.randint(30, 120),  # minutes
                    'distance': random.randint(5, 25) if activity_type in ['running', 'cycling'] else None,
                    'calories_burned': random.randint(200, 800),
                    'date': datetime.now() - timedelta(days=random.randint(0, 30)),
                    'notes': f'{user["name"]} completed {activity_type} session'
                })
        
        db.activities.insert_many(activities_data)

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = []
        
        for user in users_data:
            total_points = random.randint(500, 2000)
            leaderboard_data.append({
                'user_id': user['_id'],
                'team_id': user['team_id'],
                'total_points': total_points,
                'weekly_points': random.randint(100, 500),
                'monthly_points': random.randint(300, 1000),
                'rank': 0,  # Will be calculated
                'last_updated': datetime.now()
            })
        
        # Sort and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_points'], reverse=True)
        for rank, entry in enumerate(leaderboard_data, start=1):
            entry['rank'] = rank
        
        db.leaderboard.insert_many(leaderboard_data)

        # Create workout suggestions
        self.stdout.write('Creating workout suggestions...')
        workouts_data = [
            {
                'name': 'Iron Man Cardio Blast',
                'description': 'High-intensity interval training for endurance',
                'difficulty': 'advanced',
                'duration': 45,
                'exercises': [
                    {'name': 'Burpees', 'reps': 20, 'sets': 3},
                    {'name': 'Mountain Climbers', 'reps': 30, 'sets': 3},
                    {'name': 'Jump Squats', 'reps': 15, 'sets': 3}
                ],
                'target_audience': 'advanced',
                'created_at': datetime.now()
            },
            {
                'name': 'Spider-Sense Agility Training',
                'description': 'Improve reflexes and agility',
                'difficulty': 'intermediate',
                'duration': 40,
                'exercises': [
                    {'name': 'Ladder Drills', 'duration': '5 minutes'},
                    {'name': 'Box Jumps', 'reps': 15, 'sets': 4},
                    {'name': 'Lateral Bounds', 'reps': 20, 'sets': 3}
                ],
                'target_audience': 'intermediate',
                'created_at': datetime.now()
            },
            {
                'name': 'Hulk Strength Builder',
                'description': 'Build raw strength and power',
                'difficulty': 'expert',
                'duration': 60,
                'exercises': [
                    {'name': 'Deadlifts', 'reps': 8, 'sets': 5},
                    {'name': 'Bench Press', 'reps': 10, 'sets': 4},
                    {'name': 'Squats', 'reps': 12, 'sets': 4}
                ],
                'target_audience': 'expert',
                'created_at': datetime.now()
            },
            {
                'name': 'Batman Combat Conditioning',
                'description': 'Mixed martial arts conditioning',
                'difficulty': 'expert',
                'duration': 50,
                'exercises': [
                    {'name': 'Heavy Bag Work', 'duration': '10 minutes'},
                    {'name': 'Shadow Boxing', 'duration': '5 minutes'},
                    {'name': 'Grappling Drills', 'duration': '10 minutes'}
                ],
                'target_audience': 'expert',
                'created_at': datetime.now()
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Sprint and speed development',
                'difficulty': 'advanced',
                'duration': 35,
                'exercises': [
                    {'name': 'Sprint Intervals', 'duration': '15 minutes'},
                    {'name': 'High Knees', 'reps': 50, 'sets': 3},
                    {'name': 'Acceleration Drills', 'duration': '10 minutes'}
                ],
                'target_audience': 'advanced',
                'created_at': datetime.now()
            },
            {
                'name': 'Wonder Woman Warrior Workout',
                'description': 'Full-body functional strength',
                'difficulty': 'advanced',
                'duration': 55,
                'exercises': [
                    {'name': 'Olympic Lifts', 'reps': 8, 'sets': 4},
                    {'name': 'Pull-ups', 'reps': 12, 'sets': 4},
                    {'name': 'Lunges', 'reps': 20, 'sets': 3}
                ],
                'target_audience': 'advanced',
                'created_at': datetime.now()
            },
            {
                'name': 'Aquaman Underwater Endurance',
                'description': 'Swimming and water-based training',
                'difficulty': 'intermediate',
                'duration': 45,
                'exercises': [
                    {'name': 'Freestyle Laps', 'distance': '1000m'},
                    {'name': 'Underwater Swimming', 'distance': '50m', 'sets': 5},
                    {'name': 'Treading Water', 'duration': '10 minutes'}
                ],
                'target_audience': 'intermediate',
                'created_at': datetime.now()
            },
            {
                'name': 'Black Widow Flexibility & Control',
                'description': 'Flexibility and body control training',
                'difficulty': 'intermediate',
                'duration': 40,
                'exercises': [
                    {'name': 'Yoga Flow', 'duration': '15 minutes'},
                    {'name': 'Pike Stretch', 'duration': '5 minutes'},
                    {'name': 'Handstand Practice', 'duration': '10 minutes'}
                ],
                'target_audience': 'intermediate',
                'created_at': datetime.now()
            }
        ]
        db.workouts.insert_many(workouts_data)

        # Summary
        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully!'))
        self.stdout.write(f'Teams created: {db.teams.count_documents({})}')
        self.stdout.write(f'Users created: {db.users.count_documents({})}')
        self.stdout.write(f'Activities created: {db.activities.count_documents({})}')
        self.stdout.write(f'Leaderboard entries created: {db.leaderboard.count_documents({})}')
        self.stdout.write(f'Workouts created: {db.workouts.count_documents({})}')
        
        client.close()
