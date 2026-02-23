from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    """Сериализатор модели пользователя"""

    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор модели платежей"""

    class Meta:
        model = Payment
        fields = "__all__"
