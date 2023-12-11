from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError, force_str, smart_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.models import OneTimePassword, User
from .serializers import (
    UserSerializers,
    LoginSerializer,
    LogoutUserSerializer,
    PasswordResetRequestSerializer,
    SetNewPasswordSerializer,
)

from rest_framework.exceptions import AuthenticationFailed
from .utils import send_code_to_user, send_normal_email


class RegistrationView(GenericAPIView):
    serializer_class = UserSerializers

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_code_to_user(user.email)

            response_data = {
                "data": UserSerializers(user).data,
                "message": f"Dear {user.first_name}, thanks for signing up. A pass code has been sent to your email.",
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otp_code = request.data.get("otp")

        try:
            user_code_obj = OneTimePassword.objects.get(code=otp_code)
            user = user_code_obj.user

            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(
                    {"message": "Account email verified successfully"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "User is already verified"},
                    status=status.HTTP_200_OK,
                )

        except OneTimePassword.DoesNotExist:
            return Response(
                {"message": "Passcode not provided"},
                status=status.HTTP_404_NOT_FOUND,
            )


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestAuthenticationView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"msg": "it works"}
        return Response(data, status=status.HTTP_200_OK)


class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "A link has been sent to your email to reset your password"},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirm(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            # Ensure uidb64 and token are strings
            uid = force_str(urlsafe_base64_decode(uidb64), "utf-8")
            token = force_str(token)

            # Print values for debugging
            print("UID:", uid)
            print("Token:", token)

            # Decode uid to obtain user_id
            user = User.objects.get(id=uid)

            # Instantiate the PasswordResetTokenGenerator
            token_generator = PasswordResetTokenGenerator()

            # Ensure token is a valid token for the user
            if not token_generator.check_token(user, token):
                return Response(
                    {"message": "Token is invalid or has expired"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            return Response(
                {
                    "success": True,
                    "message": "Valid credentials",
                    "uidb64": uidb64,
                    "token": token,
                },
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except DjangoUnicodeDecodeError as e:
            return Response(
                {"message": "Token is invalid or has expired"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class SetNewPassword(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {"message": "Password reset successfully"},
            status=status.HTTP_200_OK,
        )


class LogoutUserView(GenericAPIView):
    serializer_class=LogoutUserSerializer
    permission_classes=[IsAuthenticated]
    
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)