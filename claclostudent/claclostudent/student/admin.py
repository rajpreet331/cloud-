# student/admin.py
from django.contrib import admin
from .models import Student, Course, Enrollment, LearningResource, Exercise, Assignment, Grade

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(LearningResource)
admin.site.register(Exercise)
admin.site.register(Assignment)
admin.site.register(Grade)