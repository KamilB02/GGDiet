from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

def __str__(self):
    return self.title

class DietPlan(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    target_weight = models.FloatField()
    dietary_restrictions = models.CharField(max_length=255, blank=True)
    speed_of_weight_loss = models.CharField(max_length=50)

    def __str__(self):
        return f"Diet Plan for user with target weight {self.target_weight} kg"