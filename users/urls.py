from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    CreatePaymentView,
    PaymentListAPIView,
    UserCreateAPIView,
    UserViewSet,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payment-list"),
    path("payments/create/", CreatePaymentView.as_view(), name="payment-create"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
] + router.urls
