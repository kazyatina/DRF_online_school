from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter

from users.models import Payment, User

from .serializers import PaymentSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Список пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListAPIView(generics.ListAPIView):
    """Список платежей"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("lesson", "course", "payment_method")
    ordering_fields = ("payment_date",)
