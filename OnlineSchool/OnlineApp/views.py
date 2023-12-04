from django.shortcuts import render
from .models import Course

def Admin(request):
    return render(request, 'OnlineApp/Admin.html')

def Home(request):
    courses = Course.objects.all  # Fetch all courses from the database
    return render(request, 'OnlineApp/Home1.html', {'course': courses})

# def Courses(request):
#     courses = Course.objects.all  # Fetch all courses from the database
#     return render(request, 'OnlineApp/course.html', {'course': courses})

def Courses(request):
    courses = Course.objects.all()  # Fetch the course data from your database
    context = {'course': courses}
    return render(request, 'OnlineApp/course.html', context)