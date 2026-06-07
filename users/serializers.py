from datetime import date

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'birth_date', 'can_be_contacted', 'can_data_be_shared']

    password = serializers.CharField(write_only=True)

    def validate_birth_date(self, birth_date):
        today = date.today()
        age = (today.year - birth_date.year -
               ((today.month, today.day) < (birth_date.month, birth_date.day)))
        if age < 15:
            raise serializers.ValidationError("L'utilisateur doit avoir au moins 15 ans.")
        else:
            return birth_date

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
