from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'team_id', 'team_name', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_team_name(self, obj):
        if obj.team_id:
            try:
                team = Team.objects.get(_id=obj.team_id)
                return team.name
            except Team.DoesNotExist:
                return None
        return None
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'member_count', 'created_at', 'updated_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_member_count(self, obj):
        return User.objects.filter(team_id=str(obj._id)).count()


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    calories_burned = serializers.IntegerField(source='calories', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'user_name', 'team_id', 'activity_type', 'duration', 
                  'distance', 'calories', 'calories_burned', 'date', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_name(self, obj):
        try:
            user = User.objects.get(_id=obj.user_id)
            return user.name
        except User.DoesNotExist:
            return "Unknown User"


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user_name', 'team_id', 'team_name', 'total_activities', 
                  'total_duration', 'total_distance', 'total_calories', 'rank', 'updated_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_name(self, obj):
        try:
            user = User.objects.get(_id=obj.user_id)
            return user.name
        except User.DoesNotExist:
            return "Unknown User"
    
    def get_team_name(self, obj):
        if obj.team_id:
            try:
                team = Team.objects.get(_id=obj.team_id)
                return team.name
            except Team.DoesNotExist:
                return None
        return None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    name = serializers.CharField(source='title', read_only=True)
    category = serializers.CharField(source='workout_type', read_only=True)
    duration = serializers.IntegerField(source='estimated_duration', read_only=True)
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'user_id', 'user_name', 'title', 'name', 'description', 'workout_type',
                  'category', 'difficulty', 'estimated_duration', 'duration', 'suggested_date', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_name(self, obj):
        try:
            user = User.objects.get(_id=obj.user_id)
            return user.name
        except User.DoesNotExist:
            return "Unknown User"
