from django.urls import path
from. import views


urlpatterns = [
    path('', views.Admin, name= 'admin-login'),
    path('home', views.Home, name= 'Home'),
    path('login', views.Admin, name= 'admin-login'),

    #  display all course as a list 
    #  path('course', views.courses),

    # show course details, course teacher details, and list of students in this couse
    # path('course/show', views.showCourse),
    
    
]
