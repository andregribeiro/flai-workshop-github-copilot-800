from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['username', 'email']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_type', 'user_id', 'team_id', 'duration', 'distance', 'calories', 'date', 'created_at']
    list_filter = ['activity_type', 'date', 'created_at']
    search_fields = ['user_id', 'team_id', 'activity_type']
    ordering = ['-date']
    readonly_fields = ['created_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'user_id', 'team_id', 'total_activities', 'total_duration', 
                    'total_distance', 'total_calories', 'updated_at']
    list_filter = ['rank', 'updated_at']
    search_fields = ['user_id', 'team_id']
    ordering = ['rank']
    readonly_fields = ['updated_at']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'user_id', 'workout_type', 'difficulty', 
                    'estimated_duration', 'suggested_date', 'created_at']
    list_filter = ['workout_type', 'difficulty', 'created_at']
    search_fields = ['title', 'user_id', 'workout_type', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
