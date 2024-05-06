# student/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            student_id = form.cleaned_data.get('student_id')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            student = Student.objects.create(
                user=user,
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number
            )
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'student/login.html', {'form': form})


@login_required
def index_view(request):
    return render(request, 'student/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(user=user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})

@login_required
def profile_view(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'student/profile.html', {'form': form})

@login_required
def enroll_course_view(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user.student
            enrollment.save()
            return redirect('index')
    else:
        form = EnrollmentForm()
    return render(request, 'student/enroll_course.html', {'form': form})

@login_required
def submit_assignment_view(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.exercise = exercise
            assignment.student = student
            assignment.save()
            return redirect('index')
    else:
        form = AssignmentForm()
    return render(request, 'student/submit_assignment.html', {'form': form, 'exercise': exercise})


@login_required
def learning_resources_view(request):
    resources = LearningResource.objects.all()
    return render(request, 'student/learning_resources.html', {'resources': resources})

@login_required
def exercises_view(request):
    exercises = Exercise.objects.all()
    return render(request, 'student/exercises.html', {'exercises': exercises})

@login_required
def grades_view(request):
    student = get_object_or_404(Student, user=request.user)
    assignments = Assignment.objects.filter(student=student)
    grades = Grade.objects.filter(assignment__in=assignments)
    return render(request, 'student/grades.html', {'grades': grades})


@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('index')
