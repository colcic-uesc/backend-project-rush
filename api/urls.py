from django.urls import path

from .views import (
    DepartmentView,
    DepartmentDetailView,
    CourseView,
    CourseDetailView,
    SkillView,
    SkillDetailView,
    StudentView,
    StudentDetailView,
    LogView
)

urlpatterns = [
    path('departments/', DepartmentView.as_view(),
         name='departments'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(),
         name='department-detail'),
    path('courses/', CourseView.as_view(),
         name='courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(),
         name='course-detail'),
    path('skills/', SkillView.as_view(),
         name='skills'),
    path('skills/<int:pk>/', SkillDetailView.as_view(),
         name='skill-detail'),
    path('students/', StudentView.as_view(),
         name='students'),
    path('students/<int:pk>/', StudentDetailView.as_view(),
         name='student-detail'),
    path('logs/', LogView.as_view(),
         name='logs'),
]
