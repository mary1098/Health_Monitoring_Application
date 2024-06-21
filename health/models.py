from django.db import models

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()

class HealthData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    symptom = models.CharField(max_length=255)
    description = models.TextField()
    recorded_at = models.DateTimeField(auto_now_add=True)
