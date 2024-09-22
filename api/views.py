from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import permissions, status

from .models import (
    Department,
    Course,
    Professor,
    Student,
    Project,
    Skill
)

from .serializers import (
    DepartmentSerializer,
    CourseSerializer,
    ProfessorSerializer,
    StudentSerializer,
    ProjectSerializer,
    SkillSerializer,
)


class DepartamentView(APIView):
    query_set = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = DepartmentSerializer(self.query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DepartmentDetailView(APIView):
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
