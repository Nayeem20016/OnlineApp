from django import forms
from .models import Course, Student, Teacher

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'credits', 'department']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'department', 'courses']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'department', 'courses']

