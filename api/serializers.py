from django.contrib.auth.models import User
from .models import DietPlan, UserInfo,Meal
from rest_framework import serializers

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['weight', 'height', 'age', 'gender', 'physical_activity_at_work', 'physical_activity_in_free_time', 'objective']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'calories', 'macros_protein', 'macros_carbs', 'macros_fats', 'ingredients']

class DietPlanSerializer(serializers.ModelSerializer):
    breakfast1 = MealSerializer(many=True)
    breakfast2 = MealSerializer(many=True)
    lunch = MealSerializer(many=True)
    tea = MealSerializer(many=True)
    dinner = MealSerializer(many=True)

    class Meta:
        model = DietPlan
        fields = ['id', 'name', 'calories_total', 'macros_protein', 'macros_carbs', 'macros_fats',
                  'breakfast1', 'breakfast2', 'lunch', 'tea', 'dinner']