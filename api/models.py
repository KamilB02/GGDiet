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
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    macros_protein = models.FloatField()
    macros_carbs = models.FloatField()
    macros_fats = models.FloatField()
    ingredients = models.JSONField()  # Przechowywanie składników jako lista

    def __str__(self):
        return self.name


class DietPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    calories_total = models.IntegerField()
    macros_protein = models.FloatField()
    macros_carbs = models.FloatField()
    macros_fats = models.FloatField()
    breakfast1 = models.ManyToManyField(Meal, related_name='breakfast1_meals', blank=True)
    breakfast2 = models.ManyToManyField(Meal, related_name='breakfast2_meals', blank=True)
    lunch = models.ManyToManyField(Meal, related_name='lunch_meals', blank=True)
    tea = models.ManyToManyField(Meal, related_name='tea_meals', blank=True)
    dinner = models.ManyToManyField(Meal, related_name='dinner_meals', blank=True)

    def __str__(self):
        return self.name