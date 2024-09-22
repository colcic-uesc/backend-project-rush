from django.urls import path
from .views import (
    DepartamentView,
    DepartmentDetailView
)

urlpatterns = [
    path('departaments/', DepartamentView.as_view(), name='departments'),
    path('departaments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]
