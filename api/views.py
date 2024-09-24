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
                        Skill(name="Python"),
                        Skill(name="Java"),
                        Skill(name="C++"),
                    ]
                ),
            ]
    }
]


class StudentView(APIView):
    query_set = DB[0]["Student"]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = StudentSerializer(self.query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillView(APIView):
    query_set = DB[0]["Skill"]
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = SkillSerializer(self.query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

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
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SkillSerializer(skill, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            skill = self.get_object(pk)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.query_set.remove(skill)
        return Response(status=status.HTTP_204_NO_CONTENT)
