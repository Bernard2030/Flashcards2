from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)
    first_name = serializers.CharField(max_length=255, min_length=3)
    last_name = serializers.CharField(max_length=255, min_length=3)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'
        ]
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError ({'email',('Email is already in use!!')})
        return super().validate(attrs) 
    def create(self, validated_data):
        return User.objects.create_user(validated_data)         

