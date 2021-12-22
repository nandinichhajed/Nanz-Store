from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentcation_classes, permission_classes

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = CustomUser
            fields = ('name', 'email', 'password', 'phone', 'gender', 'is_active', 'is_staff', 'is_superuser')
            
    
    