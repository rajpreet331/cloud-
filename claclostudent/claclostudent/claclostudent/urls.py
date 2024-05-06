# claclostudent/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from student import views as student_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', student_views.signup_view, name='signup'),
    path('accounts/login/', student_views.login_view, name='login'),
    path('accounts/logout/', student_views.custom_logout_view, name='logout'),
    path('', student_views.index_view, name='index'),
    path('profile/', student_views.profile_view, name='profile'),
    path('enroll-course/', student_views.enroll_course_view, name='enroll_course'),
    path('submit-assignment/<int:exercise_id>/', student_views.submit_assignment_view, name='submit_assignment'),
    path('learning-resources/', student_views.learning_resources_view, name='learning_resources'),
    path('exercises/', student_views.exercises_view, name='exercises'),
    path('grades/', student_views.grades_view, name='grades'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)