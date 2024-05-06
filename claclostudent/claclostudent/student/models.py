# student/models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} (Student)"

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}"

class LearningResource(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to='learning_resources/', null=True, blank=True)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='learning_resources')

    def __str__(self):
        return self.title

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return self.title

class Assignment(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments/')
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.exercise.title}"

class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank=True)
    graded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='graded_assignments')

    def __str__(self):
        return f"{self.assignment.student.user.username} - {self.assignment.exercise.title} - {self.score}"