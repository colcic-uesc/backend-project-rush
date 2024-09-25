from django.urls import path
from .views import (
    SkillView,
    SkillDetailView,
    StudentView,
    StudentDetailView
)

urlpatterns = [
    path('skills/', SkillView.as_view(), name='skills'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    path('students/', StudentView.as_view(), name='students'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
