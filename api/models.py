from django.db import models
from django.contrib.auth.models import User

def __str__(self):
    return self.title

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    age = models.FloatField()
    gender = models.CharField(max_length=10, choices=[('man', 'Man'), ('woman', 'Woman')])
    physical_activity_at_work = models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Moderate'), (3, 'High'), (4, 'Very High')])
    physical_activity_in_free_time = models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Moderate'), (3, 'Active'), (4, 'Very Active'), (5, 'Extreme')])
    objective = models.CharField(max_length=10, choices=[('less', 'Lose weight'), ('same', 'Maintain weight'), ('more', 'Gain weight')])

    def __str__(self):
        return f"{self.user.username}'s Information"


class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()

    def __str__(self):
        return self.name


class DietPlan(models.Model):
    # Pola modelu
    meals = models.ManyToManyField(Meal)
    total_calories = models.IntegerField()
    total_protein = models.IntegerField()

    def to_dict(self):
        return {
            'meals': [meal.name for meal in self.meals.all()],
            'total_calories': self.total_calories,
            'total_protein': self.total_protein,
            # dodaj inne pola, które chcesz zawrzeć
        }

    def __str__(self):
        return f"Diet Plan for user with target weight {self.target_weight} kg"