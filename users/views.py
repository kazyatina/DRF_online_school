from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import Payment, User

from .serializers import PaymentSerializer, UserCreateSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Список пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Регистрация пользователей"""

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentListAPIView(generics.ListAPIView):
    """Список платежей"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("lesson", "course", "payment_method")
    ordering_fields = ("payment_date",)
