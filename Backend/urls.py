
from django.contrib import admin
from django.urls import path, include
from api.views import RegisterView, GenerateDietView, UserInfoView, save_diet
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import CustomTokenObtainPairView
from api.services.all_recipes import AllRecipesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', CustomTokenObtainPairView .as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include("rest_framework.urls")),
    path('api/generate-diet/', GenerateDietView.as_view(), name='generate_diet'),
    path('api/user-info/', UserInfoView.as_view(), name='user_info'),
    path('api/all_recipes/', AllRecipesView.as_view(), name='all_recipes'),
    path('api/save_diet/', save_diet, name='save_diet'),
]
