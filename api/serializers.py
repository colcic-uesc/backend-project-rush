from rest_framework import serializers

from core.Skill import Skill
from core.Student import Student


class SkillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Skill(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "registration",
            "name",
            "email",
            "course",
            "bio",
            "skills"
        ]


# Ignorar para a primeira atividade, feita apenas para fins de estudo
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ["id", "name"]


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ["id", "name", "department_id"]


# class ProfessorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Professor
#         fields = ["id", "name", "email", "department", "bio"]


# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = ["id", "title", "description"]


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = [
#             "id",
#             "registration",
#             "name",
#             "email",
#             "course",
#             "bio",
#             "skills"
#         ]


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = [
#             "id",
#             "title",
#             "description",
#             "type",
#             "start_date",
#             "end_date",
#             "skills",
#             "professor_id",
#         ]
