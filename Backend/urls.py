
from django.contrib import admin
from django.urls import path, include
from api.views import RegisterView, DietPlanView, DietPlanGenerateView, UserInfoView
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import CustomTokenObtainPairView
from api.services.all_recipes import AllRecipesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', CustomTokenObtainPairView .as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include("rest_framework.urls")),
    path('api/diet-plan/', DietPlanView.as_view(), name='diet-plan'),
    path('api/user-info/', UserInfoView.as_view(), name='user_info'),
    path('api/diet-plan-generate/', DietPlanGenerateView.as_view(), name='diet-plan-generate'),
    path('api/all_recipes/', AllRecipesView.as_view(), name='all_recipes'),
]
