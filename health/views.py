from rest_framework import viewsets
from .models import UserProfile, HealthData
from .serializers import UserProfileSerializer, HealthDataSerializer
from .ai import interpret_query, suggest_health_plan
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class HealthDataViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer

@api_view(['POST'])
def interpret_query_view(request):
    query = request.data.get('query')
    result = interpret_query(query)
    return Response(result)

@api_view(['GET'])
def suggest_health_plan_view(request, user_id):
    user_profile = UserProfile.objects.get(pk=user_id)
    plans = suggest_health_plan(user_profile)
    return Response(plans)

def index(request):
    return render(request, 'index.html')