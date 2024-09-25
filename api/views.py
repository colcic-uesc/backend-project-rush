from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import permissions, status

from .serializers import (
    StudentSerializer,
    SkillSerializer,
)

from core.Student import Student
from core.Skill import Skill


DB = [
    {
        "Skill":
            [
                Skill(name="Python"),
                Skill(name="Java"),
                Skill(name="C++"),
            ],
        "Student":
            [
                Student(
                    registration="201912",
                    name="João",
                    email="joao.cic@uesc.br",
                    course="Ciência da Computação",
                    bio="Estudante de Ciência da Computação na UESC",
                    skills=[
                        0,
                        2
                    ]
                ),
            ]
    }
]


class SkillView(APIView):
    query_set = DB[0]["Skill"]
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = SkillSerializer(self.query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = SkillSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": str(e)})

        skill = serializer.save()
        self.query_set.append(skill)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillDetailView(APIView):
    query_set = DB[0]["Skill"]
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            for skill in self.query_set:
                if skill.id == pk:
                    return skill
            raise NotFound()
        except AttributeError:
            raise NotFound()

    def get(self, request, pk):
        try:
            skill = self.get_object(pk)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            skill = self.get_object(pk)
            serializer = SkillSerializer(skill, data=request.data)
            serializer.is_valid(raise_exception=True)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": str(e)})

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            skill = self.get_object(pk)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.query_set.remove(skill)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentView(APIView):
    query_set = DB[0]["Student"]
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = StudentSerializer(self.query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.validate_skills(serializer.validated_data["skills"])
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": str(e)})

        student = serializer.save()
        self.query_set.append(student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def validate_skills(self, value):
        if not all(isinstance(skill, int) for skill in value):
            raise TypeError("Skills must be integers")

        ids_skill = [skill.id for skill in DB[0]["Skill"]]

        for skill in value:
            if skill not in ids_skill:
                raise NotFound()

        return value


class StudentDetailView(APIView):
    query_set = DB[0]["Student"]
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            for student in self.query_set:
                if student.id == pk:
                    return student
            raise NotFound()
        except AttributeError:
            raise NotFound()

    def get(self, request, pk):
        try:
            student = self.get_object(pk)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            student = self.get_object(pk)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.validate_skills(serializer.validated_data["skills"])
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": str(e)})

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            student = self.get_object(pk)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.query_set.remove(student)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def validate_skills(self, value):
        if not all(isinstance(skill, int) for skill in value):
            raise TypeError("Skills must be integers")

        ids_skill = [skill.id for skill in DB[0]["Skill"]]

        for skill in value:
            if skill not in ids_skill:
                raise NotFound()

        return value
