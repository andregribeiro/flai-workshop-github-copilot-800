from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    team_id = models.CharField(max_length=24, blank=True, null=True)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(blank=True, null=True)  # in kilometers
    calories = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.activity_type} - {self.date}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    team_id = models.CharField(max_length=24, blank=True, null=True)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes
    total_distance = models.FloatField(default=0)  # in kilometers
    total_calories = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']
    
    def __str__(self):
        return f"Rank {self.rank} - User {self.user_id}"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    title = models.CharField(max_length=200)
    description = models.TextField()
    workout_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)
    estimated_duration = models.IntegerField()  # in minutes
    suggested_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
