from django.contrib import admin

from .models import (
    Department,
    Course,
    Professor,
    Skill,
    Student,
    Project,
    Log
)

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Skill)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Log)
