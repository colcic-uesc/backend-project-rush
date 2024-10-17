from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import permissions, status

from .models import (
    Department,
    Course,
    Professor,
    Skill,
    Student,
    Project,
    Log
)

from .serializers import (
    DepartmentSerializer,
    CourseSerializer,
    ProfessorSerializer,
    SkillSerializer,
    StudentSerializer,
    ProjectSerializer,
    LogSerializer
)


class DepartmentView(APIView):
    query_set = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = DepartmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
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
        try:
            department = self.get_object(pk)
            serializer = DepartmentSerializer(department)
        except NotFound:
            return Response("Department not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            department = self.get_object(pk)
            serializer = DepartmentSerializer(department, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Department not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            department = self.get_object(pk)
            serializer = DepartmentSerializer(department, data=request.data,
                                              partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Department not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            department = self.get_object(pk)
            department.delete()
        except NotFound:
            return Response("Department not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseView(APIView):
    query_set = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseDetailView(APIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        try:
            course = self.get_object(pk)
            serializer = CourseSerializer(course)
        except NotFound:
            return Response("Course not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            course = self.get_object(pk)
            serializer = CourseSerializer(course, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Course not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            course = self.get_object(pk)
            serializer = CourseSerializer(course, data=request.data,
                                          partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Course not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            course = self.get_object(pk)
            course.delete()
        except NotFound:
            return Response("Course not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillView(APIView):
    query_set = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            skills = Skill.objects.all()
            serializer = SkillSerializer(skills, many=True)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = SkillSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillDetailView(APIView):
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        try:
            skill = self.get_object(pk)
            serializer = SkillSerializer(skill)
        except NotFound:
            return Response("Skill not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            skill = self.get_object(pk)
            serializer = SkillSerializer(skill, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Skill not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            skill = self.get_object(pk)
            serializer = SkillSerializer(skill, data=request.data,
                                         partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Skill not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            skill = self.get_object(pk)
            skill.delete()
        except NotFound:
            return Response("Skill not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentView(APIView):
    query_set = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailView(APIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        try:
            student = self.get_object(pk)
            serializer = StudentSerializer(student)
        except NotFound:
            return Response("Student not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            student = self.get_object(pk)
            serializer = StudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Student not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            student = self.get_object(pk)
            serializer = StudentSerializer(student, data=request.data,
                                           partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except NotFound:
            return Response("Student not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            student = self.get_object(pk)
            student.delete()
        except NotFound:
            return Response("Student not found",
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogView(APIView):
    query_set = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            logs = Log.objects.all()
            serializer = LogSerializer(logs, many=True)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
