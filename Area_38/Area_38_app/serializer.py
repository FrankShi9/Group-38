from rest_framework import serializers

from .models import UserInfo


# send login data to front end
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
