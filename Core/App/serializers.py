from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['username' , 'email' , 'dob', 'password' ]

        def validate(self,data):
            if CustomUserModel.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError({'error': 'User already exists with this username/email '})
            return data

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Paragraph
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()