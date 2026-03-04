from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, CourseSubscription, Lesson
from materials.validators import validation_url


class LessonSerializer(ModelSerializer):
    """Сериализатор модели уроков"""

    video_url = serializers.CharField(validators=[validation_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonBriefSerializer(ModelSerializer):
    """Сериализатор модели уроков с ограниченными полями"""

    class Meta:
        model = Lesson
        fields = ("title", "description")


class CourseSerializer(ModelSerializer):
    """Сериализатор модели курсов"""

    lesson_count = SerializerMethodField()
    lessons_in_course = LessonBriefSerializer(many=True, read_only=True)
    title = serializers.CharField(validators=[validation_url])
    description = serializers.CharField(
        allow_blank=True, allow_null=True, required=False, validators=[validation_url]
    )

    def get_lesson_count(self, obj):
        lesson_count = obj.lessons.count()
        return lesson_count if lesson_count else None

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return CourseSubscription.objects.filter(
                user=request.user, course=obj
            ).exists()
        return False

    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "preview",
            "lesson_count",
            "lessons_in_course",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки"""

    class Meta:
        model = CourseSubscription
        fields = "__all__"
