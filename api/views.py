from django.shortcuts import render
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import DietPlan, UserInfo
from .serializers import DietPlanSerializer, UserInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from .services.genetic_algorithm import genetic_algorithm
from rest_framework_simplejwt.views import TokenObtainPairView
import logging


logger = logging.getLogger(__name__)
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Wywołanie oryginalnego metody w celu uzyskania tokenu
        response = super().post(request, *args, **kwargs)

        # Dodajemy nazwę użytkownika do odpowiedzi
        username = request.data.get("username")

        # Zwracamy odpowiedź z tokenem i nazwą użytkownika
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

class DietPlanView(APIView):
    def post(self, request):
        serializer = DietPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Plan dietetyczny zapisany!", "data": data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DietPlanGenerateView(APIView):
    def post(self, request):
        logger.info("DietPlanGenerateView post method was called.")
        user_requirements = request.data
        best_plan = genetic_algorithm(user_requirements)
        return Response(best_plan)

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        serializer = UserInfoSerializer(data=data)

        if serializer.is_valid():
            user_info, created = UserInfo.objects.update_or_create(user=user, defaults=serializer.validated_data)
            return Response({"message": "Informacje zostały zapisane!"}, status=200)
        return Response(serializer.errors, status=400)