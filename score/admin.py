from django.contrib import admin
from .models import Student, WrittenExam, Participation

admin.site.register([Student, WrittenExam, Participation])
