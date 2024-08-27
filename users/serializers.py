from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = obj
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate(self, data):
        name = data.get('name')
        password = data.get('password')
        user = User.objects.filter(name=name).first()

        if user is None:
            raise serializers.ValidationError("User with this name does not exist.")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")

        return user
