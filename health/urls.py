from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, HealthDataViewSet, interpret_query_view, suggest_health_plan_view
from django.urls import path
from .views import index

router = DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'health_data', HealthDataViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('interpret_query/', interpret_query_view, name='interpret_query'),
    path('suggest_health_plan/<int:user_id>/', suggest_health_plan_view, name='suggest_health_plan'),
]
