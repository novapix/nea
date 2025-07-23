from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Branch, Avatar
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['user_id'] = str(user.id)
        token['email'] = user.email
        token['role_name'] = user.role.name if user.role else ''
        token['name'] =  ''
        
        return token

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','branch_code', 'name', 'address', 'contact', 'status','branch_incharge']
        read_only_fields = ['id']

class BranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'address','contact_phone']

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['id', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)
    avatar = serializers.ImageField(source='avatar.image', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'role_name', 'avatar']
