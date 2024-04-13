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