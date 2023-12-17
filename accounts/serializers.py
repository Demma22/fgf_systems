# accounts/serializers.py
from rest_framework import serializers
from .models import User, Admin, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["get_full_name"]


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["user"]


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user_type = self.context.get("user_type", "contributor")

        if user_type == "contributor":
            # Remove password2 from the validated data before creating the user
            validated_data.pop("password2", None)
            return User.objects.create_contributor(**validated_data)
        elif user_type == "admin":
            # Remove password2 from the validated data before creating the user
            validated_data.pop("password2", None)
            return User.objects.create_admin(**validated_data)
        else:
            raise serializers.ValidationError("Invalid user type")


class ContributorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SetNewPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    uidb64 = serializers.CharField()
    password = serializers.CharField(write_only=True)
