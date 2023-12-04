from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dept_name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    credits = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class TeachesCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.name} teaches {self.course.title}"


class TakesCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student.name} teaches {self.course.title}"
    
