from django.contrib import admin
from .models import Department
from .models import Course
from .models import Teacher
from .models import Student
from .models import TakesCourse
from .models import TeachesCourse

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(TakesCourse)
admin.site.register(TeachesCourse)