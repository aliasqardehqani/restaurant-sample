from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('api/', include('api.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/rest-auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),

]
