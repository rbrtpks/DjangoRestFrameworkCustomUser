from rest_framework.serializers import ModelSerializer
from users.models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'fone', 'is_staff', 'first_name', 'last_name')
