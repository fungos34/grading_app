from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    immatriculation_number = models.IntegerField(primary_key=True, null=False)
    notes = models.CharField(max_length=128)
    student_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    
class WrittenExam(models.Model):
    exam_date = models.DateField(null=False)
    exam_number = models.IntegerField(null=False)
    exam_topic = models.CharField(max_length=128, null=False)
    reached_points = models.FloatField(max_length=5, null=True)
    max_points = models.FloatField(max_length=5, default=10, null=False)
    exam_front_page = models.ImageField(null=True, blank=True)
    exam_back_page = models.ImageField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.student}:exam{self.exam_number}"

class Participation(models.Model):
    reached_points = models.FloatField(max_length=5, null=True)
    max_points = models.FloatField(max_length=5, default=2, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)