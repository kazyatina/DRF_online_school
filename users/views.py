from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from materials.models import Course
from users.models import Payment, User

from .serializers import (
    PaymentCreateSerializer,
    PaymentSerializer,
    UserCreateSerializer,
    UserPrivateSerializer,
    UserSerializer,
)
from .services import create_stripe_price, create_stripe_product, create_stripe_session


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Список пользователей (приватные данные)",
        responses={200: UserPrivateSerializer(many=True)},
    ),
)
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


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_description="Создать платёж за курс через Stripe. Возвращает ссылку на оплату.",
        request_body=PaymentCreateSerializer,
        responses={
            201: openapi.Response(
                description="Платёж создан",
                examples={
                    "application/json": {
                        "payment_id": 1,
                        "payment_link": "https://checkout.stripe.com/...",
                        "status": "pending",
                    }
                },
            ),
            404: "Курс не найден",
        },
    ),
)
class CreatePaymentView(generics.GenericAPIView):
    """Взаимодействие с платежным сервисом (Stripe)"""

    serializer_class = PaymentCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_id = serializer.validated_data["course_id"]
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND
            )

        product = create_stripe_product(course.title)
        amount = (
            course.price
            if (hasattr(course, "price") and course.price is not None)
            else 10
        )
        price = create_stripe_price(amount, product.id)
        success_url = "https://127.0.0.1:8000/"
        session = create_stripe_session(price.id)

        payment = Payment.objects.create(
            user=request.user,
            course=course,
            amount=amount,
            payment_method="card",  # оплата через Stripe — картой
            stripe_session_id=session.id,
            payment_link=session.url,
            status="pending",
        )

        return Response(
            {
                "payment_id": payment.id,
                "payment_link": payment.payment_link,
                "status": payment.status,
            },
            status=status.HTTP_201_CREATED,
        )
