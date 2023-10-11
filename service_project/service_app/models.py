from django.db import models
from django.contrib.auth.models import User
#from django_extensions.db.fields import AutoSlugField
#from django_extensions.db.fields import AutoSlugField

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="courses")


class Consultation(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE
    )  # Добавляем поле course
    date = models.DateTimeField()
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)


class Report(models.Model):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to="reports/")
    created_at = models.DateTimeField(auto_now_add=True)


class ConsultationBooking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    attachments = models.FileField(upload_to="assignments/")
    created_at = models.DateTimeField(auto_now_add=True)
