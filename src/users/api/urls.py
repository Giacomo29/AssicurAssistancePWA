from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.api.views import (
    CurrentUserAPIView, RegisterAPIView,
    LoginAPIView, VerifyEmail, PasswordTokenCheckAPI,
    RequestPasswordResetEmail, SetNewPasswordAPIView,
    UserDetailView, ChangeAvatarAPIView,
    LogoutAPIView, ChangePasswordView,
)
from users.consumers import Notification

urlpatterns = [
    # Endpoint for getting the current user's details
    path("user/", CurrentUserAPIView.as_view()),

    # Endpoint for modifying user details
    path('modifica-user/', UserDetailView.as_view(), name='user-detail'),

    # Endpoint for changing user's avatar
    path('user/avatar/', ChangeAvatarAPIView.as_view(), name='user-avatar'),

    # Endpoint for user registration
    path('register/', RegisterAPIView.as_view()),

    # Endpoint for user login
    path('entra/', LoginAPIView.as_view(), name='token_obtain_pair'),

    # Endpoint for refreshing JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint for changing user's password
    path('user/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

    # Endpoint for verifying user's email
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),

    # Endpoint for requesting password reset email
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),

    # Endpoint for verifying password reset token
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),

    # Endpoint for setting new password after reset
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),

    # Endpoint for user logout
    path('esci/', LogoutAPIView.as_view(), name='logout'),

    # Endpoint for adding notification (WebSocket endpoint)
    path('add-notification/', Notification.as_asgi()),
]
