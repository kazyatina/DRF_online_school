from django.db import models
from django.db.models import CASCADE

from users.models import User


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание курса",
    )
    preview = models.ImageField(
        upload_to="materials/previews/",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Превью",
    )
    owner = models.ForeignKey(
        User, on_delete=CASCADE, verbose_name="Владелец", null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="lessons",
        verbose_name="Курс",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = (
        models.TextField(
            blank=True,
            null=True,
            verbose_name="Описание урока",
            help_text="Введите описание урока",
        ),
    )

    preview = models.ImageField(
        upload_to="materials/previews/",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Превью",
    )
    video_url = models.URLField(verbose_name="Ссылка на видео урока")
    owner = models.ForeignKey(
        User, on_delete=CASCADE, verbose_name="Владелец", null=True, blank=True
    )

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
