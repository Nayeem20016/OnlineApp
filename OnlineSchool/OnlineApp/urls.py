from django.urls import path
from . import views


urlpatterns = [
    path('', views.Admin, name= 'admin-login'),
    path('home', views.Home, name= 'Home'),
    path('login', views.Admin, name= 'admin-login'),
    path('course', views.Courses, name= 'course'),
    path('teacher', views.Teachers, name= 'teacher'),
    path('student', views.Students, name= 'student'),
    

   
    
    
]
