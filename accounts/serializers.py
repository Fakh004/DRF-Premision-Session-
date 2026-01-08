from rest_framework import serializers
from .models import User, UserProfile
# from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def validate(self, instance):
        password = instance.get('password')
        password2 = instance.pop('confirm_password')
        if not password == password2:
            raise serializers.ValidationError("Passwords do not match")
        # instance['password'] = make_password(instance['password'])
        return super().validate(instance)
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')