from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Student(models.Model):
    registration = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    skills = models.ManyToManyField(Skill)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Log(models.Model):
    client_ip = models.CharField(max_length=100)
    has_jwt = models.BooleanField()
    request_date = models.DateTimeField()
    request_method = models.CharField(max_length=100)
    request_total_time = models.DurationField()
