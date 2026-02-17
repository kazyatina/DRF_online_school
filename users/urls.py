from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"payments", PaymentListAPIView)

urlpatterns = [] + router.urls
