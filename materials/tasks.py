import logging
from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User

logger = logging.getLogger(__name__)


@shared_task
def send_course_update_email(user_email, course_title):
    """Рассылка писем пользователям об обновлении материалов курса"""
    subject = f"Обновление курса {course_title}"
    message = f"Здравствуйте! В курсе '{course_title}' появились обновления."
    from_email = EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def check_last_login():
    one_month_ago = timezone.now() - timedelta(days=30)
    users_no_active = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    updated_count = users_no_active.update(is_active=False)

    return f"{updated_count} users deactivated"
