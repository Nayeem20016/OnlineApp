
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('OnlineApp.urls')),
    path('login', include('OnlineApp.urls')),
    path('home', include('OnlineApp.urls')),
    path('admin/', admin.site.urls),
]
