from rest_framework import serializers

from .models import (
    Department,
    Course,
    Professor,
    Skill,
    Student,
    Project,
)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "department_id"]


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ["id", "name", "email", "department", "bio"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "title", "description"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "registration",
            "name",
            "email",
            "course",
            "bio",
            "skills"
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "start_date",
            "end_date",
            "skills",
            "professor_id",
        ]
