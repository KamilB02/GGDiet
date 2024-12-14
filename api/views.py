from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from .services.genetic_algorithm import genetic_algorithm, prepare_user_requirements, used_recipes
from .services.user_required import calculate_macro, calculate_calories
from rest_framework_simplejwt.views import TokenObtainPairView
import logging
import uuid
import concurrent.futures


logger = logging.getLogger(__name__)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        username = request.data.get("username")

        return Response({
            'access': response.data['access'],
            'refresh': response.data['refresh'],
            'username': username
        })


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_info = UserInfo.objects.get(user=user)
            serializer = UserInfoSerializer(user_info)
            return Response(serializer.data, status=200)
        except UserInfo.DoesNotExist:
            return Response({"message": "Nie znaleziono informacji o użytkowniku."}, status=404)
    def post(self, request):
        user = request.user
        data = request.data
        serializer = UserInfoSerializer(data=data)

        if serializer.is_valid():
            user_info, created = UserInfo.objects.update_or_create(user=user, defaults=serializer.validated_data)
            return Response({"message": "Informacje zostały zapisane!"}, status=200)
        return Response(serializer.errors, status=400)


class GenerateDietView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user
        user_info = UserInfo.objects.get(user=user)

        user_data = {
            'weight': user_info.weight,
            'height': user_info.height,
            'age': user_info.age,
            'gender': user_info.gender,
            'physical_activity_at_work': user_info.physical_activity_at_work,
            'physical_activity_in_free_time': user_info.physical_activity_in_free_time,
            'objective': user_info.objective,
        }

        daily_calories = calculate_calories(user_data)
        daily_macros = calculate_macro(user_data)

        preferences = request.data

        preferences.update({
            'calories': daily_calories,
            'protein': daily_macros[0],
            'carbs': daily_macros[1],
            'fats': daily_macros[2],
        })

        def run_genetic_algorithm(user_requirements):
            return [genetic_algorithm(user_requirements, _, 2000, 1000, 4, 5) for _ in range(3)]

        user_requirements = prepare_user_requirements(preferences)
        diet_plans = run_genetic_algorithm(user_requirements)

        used_recipes.clear()

        if diet_plans is None:
            return JsonResponse({'error': 'Operacja przekroczyła limit czasu'}, status=status.HTTP_408_REQUEST_TIMEOUT)

        return JsonResponse( {'diet_plans': diet_plans}, status=status.HTTP_200_OK)
