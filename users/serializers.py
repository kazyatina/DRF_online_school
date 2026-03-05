from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор модели платежей"""

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentCreateSerializer(Serializer):
    """Сериализатор создания платежей"""

    course_id = serializers.IntegerField()


class UserSerializer(ModelSerializer):
    """Сериализатор модели пользователя"""

    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(ModelSerializer):
    """Сериализатор создания пользователя"""

    class Meta:
        model = User
        fields = "__all__"


class UserPrivateSerializer(ModelSerializer):
    """Сериализатор платежей пользователя (приватные данные)"""

    payments_of_user = SerializerMethodField()

    def get_payments_of_user(self, obj):
        payments = Payment.objects.filter(user=obj)
        serializer = PaymentSerializer(payments, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = "__all__"
