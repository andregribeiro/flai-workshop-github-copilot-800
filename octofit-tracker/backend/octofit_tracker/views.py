from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific user"""
        activities = Activity.objects.filter(user_id=str(pk))
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def workouts(self, request, pk=None):
        """Get all workouts for a specific user"""
        workouts = Workout.objects.filter(user_id=str(pk))
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific team"""
        activities = Activity.objects.filter(team_id=str(pk))
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def leaderboard(self, request, pk=None):
        """Get leaderboard for a specific team"""
        leaderboard = Leaderboard.objects.filter(team_id=str(pk))
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent activities"""
        activities = Activity.objects.all()[:10]
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get activities grouped by type"""
        activity_type = request.query_params.get('type', None)
        if activity_type:
            activities = Activity.objects.filter(activity_type=activity_type)
        else:
            activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    
    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top performers"""
        limit = int(request.query_params.get('limit', 10))
        leaderboard = Leaderboard.objects.all()[:limit]
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def update_rankings(self, request):
        """Update leaderboard rankings based on activities"""
        # This would contain logic to recalculate rankings
        # For now, just return success
        return Response({'message': 'Rankings updated successfully'}, status=status.HTTP_200_OK)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    @action(detail=False, methods=['get'])
    def suggested(self, request):
        """Get suggested workouts"""
        user_id = request.query_params.get('user_id', None)
        if user_id:
            workouts = Workout.objects.filter(user_id=user_id)
        else:
            workouts = Workout.objects.all()[:5]
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts filtered by difficulty"""
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            workouts = Workout.objects.filter(difficulty=difficulty)
        else:
            workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
