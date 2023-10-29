from django.contrib import admin
from .models import Department, Course, Teacher, Student, TakesCourse, TeachesCourse

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(TakesCourse)
admin.site.register(TeachesCourse)