from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """Сериализатор модели уроков"""

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    """Сериализатор модели курсов"""

    lesson_count = SerializerMethodField()
    lessons_in_course = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        lesson_count = obj.lessons.count()
        return lesson_count if lesson_count else None

    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "preview",
            "lesson_count",
            "lessons_in_course",
        )
