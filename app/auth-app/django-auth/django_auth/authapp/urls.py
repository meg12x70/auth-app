from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('appusers/<int:pk>', AppUserRetrieveView.as_view()),
    path('appusers/update/<int:pk>', AppUserUpdateView.as_view()),
    path('appusers/all/', AppUserListView.as_view()),
    path('appusers/new/', CreateAppUserView.as_view()),
]