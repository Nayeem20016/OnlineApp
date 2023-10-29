# Generated by Django 4.2.5 on 2023-10-29 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('credits', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.department')),
            ],
        ),
        migrations.CreateModel(
            name='TeachesCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.course')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TakesCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineApp.department'),
        ),
    ]
