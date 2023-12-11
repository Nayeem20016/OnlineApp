from django.shortcuts import render, redirect
from .models import Course, Student, Teacher
from .forms import CourseForm, StudentForm, TeacherForm  


def Admin(request):
    return render(request, 'OnlineApp/Admin.html')

def Home(request):
    courses = Course.objects.all  
    return render(request, 'OnlineApp/Home.html', {'course': courses})

def Courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')  
    else:
        form = CourseForm()

    courses = Course.objects.all()
    context = {'course': courses, 'form': form}
    return render(request, 'OnlineApp/course.html', context)

def Students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')  
    else:
        form = StudentForm()

    students = Student.objects.all()
    context = {'student': students, 'form': form}
    return render(request, 'OnlineApp/student.html', context)

def Teachers(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')  
    else:
        form = TeacherForm()

    teachers = Teacher.objects.all()
    context = {'teacher': teachers, 'form': form}
    return render(request, 'OnlineApp/teacher.html', context)
