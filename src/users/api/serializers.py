from requests import Response
from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.password_validation import validate_password


class UserDisplaySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user information.
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'nome', 'cognome', 'avatar']


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model.
    """

    avatar = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'nome', 'cognome', 'avatar']


class AvatarSerializer(serializers.ModelSerializer):
    """
    Serializer for updating avatar.
    """

    class Meta:
        model = CustomUser
        fields = ['avatar']

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class CreateCustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating CustomUser.
    """

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'nome', 'cognome', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'])
        user.set_password(validated_data['password'])
        user.nome = validated_data.get('nome', '')
        user.cognome = validated_data.get('cognome', '')
        user.save()
        return user


class UpdateCustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for updating CustomUser.
    """

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'nome', 'cognome', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cognome = validated_data.get('cognome', instance.cognome)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class LoginCustomUserSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials.")


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    """
    Serializer for reset password email request.
    """

    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    """
    Serializer for setting a new password.
    """

    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            id = force_str(urlsafe_base64_decode(uidb64).decode())
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            user.set_password(password)
            user.save()
            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for changing password.
    """

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
