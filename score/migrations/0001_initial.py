# Generated by Django 4.2.6 on 2024-05-17 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('immatriculation_number', models.IntegerField(primary_key=True, serialize=False)),
                ('notes', models.CharField(max_length=128, null=True)),
                ('student_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WrittenExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('exam_number', models.IntegerField()),
                ('exam_topic', models.CharField(max_length=128)),
                ('reached_points', models.FloatField(max_length=5, null=True)),
                ('max_points', models.FloatField(default=10, max_length=5)),
                ('exam_front_page', models.ImageField(null=True, upload_to='')),
                ('exam_back_page', models.ImageField(null=True, upload_to='')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.student')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reached_points', models.FloatField(max_length=5, null=True)),
                ('max_points', models.FloatField(default=2, max_length=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.student')),
            ],
        ),
    ]
