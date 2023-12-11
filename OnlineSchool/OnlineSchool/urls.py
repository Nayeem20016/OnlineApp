
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OnlineApp.urls')),
    path('login', include('OnlineApp.urls')),
    path('home', include('OnlineApp.urls')),
    path('course', include('OnlineApp.urls')),
    path('teacher', include('OnlineApp.urls')),
    path('student', include('OnlineApp.urls')),

]
