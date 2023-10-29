from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)  # ADDED LATER
    dept_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dept_name


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    credits = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def dept_name(self):
    #     return self.department.dept_name

# class Section(models.Model):
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
#     sec_id = models.CharField(max_length=100)
#     semester = models.CharField(max_length=100)
#     year = models.CharField(max_length=100)

#     def __str__(self):
#         return self.sec_id

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TeachesCourse(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_id

class TakesCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.student_id