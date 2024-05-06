# student/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Enrollment, Assignment


# student/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student

class SignUpForm(UserCreationForm):
    student_id = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'student_id', 'first_name', 'last_name', 'email', 'phone_number']

class LoginForm(AuthenticationForm):
    pass

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['file', 'comments']