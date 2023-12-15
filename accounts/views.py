# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Admin, Contributor, User
from .serializers import (
    AdminLoginSerializer,
    ContributorLoginSerializer,
    PasswordResetRequestSerializer,
    RegistrationSerializer,
    SetNewPasswordSerializer,
)


class ContributorRegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class AdminRegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class ContributorLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContributorLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user and user.is_contributor:
            login(request, user)
            return Response(
                {"message": "Contributor logged in successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class AdminLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user and user.is_admin:
            login(request, user)
            return Response(
                {"message": "Admin logged in successfully"}, status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {"detail": "Successfully logged out."}, status=status.HTTP_200_OK
        )


class PasswordResetRequestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Implement your password reset email sending logic here
        return Response(
            {"message": "Password reset email sent successfully"},
            status=status.HTTP_200_OK,
        )


class SetNewPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        password = serializer.validated_data["password"]
        user.set_password(password)
        user.save()
        return Response(
            {"message": "Password reset successful"}, status=status.HTTP_200_OK
        )
