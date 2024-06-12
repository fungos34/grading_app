from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import User, WrittenExam, Participation, Student
from django.contrib.auth import login, logout, authenticate

import time

def score(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            student = list(Student.objects.filter(student_user=request.user))[0]
            exams = WrittenExam.objects.filter(student=student)
            participation = list(Participation.objects.filter(student=student))[0]
            exam_numbers = [str(exam.exam_number) for exam in exams]
            context = {
                "range": range(1,9),
                "student": student,
                "exams": exams,
                "exam_numbers": exam_numbers,
                "immatriculation_number": str(student.immatriculation_number),
                "participation": participation,
                "title": "CHE119 Beurteilungen SS2024"
            }
            return render(request, "score/index.html", context=context)
        else:
            context = {
                "title": "Anmeldung Punktestand CHE119",
                "range": range(1,9),
            }
            return render(request, "score/login.html", context=context)
    else:
        return Http404("Not available")

def log_in(request):
    if request.method == "POST":
        student_id = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=student_id, password=password)
        if user != None:
            login(request=request, user=user)
        else:
            print(f'FAILED LOG IN: {student_id} ### {password}')
        return redirect("score")
    

def log_out(request):
    if request.method == "GET":
        logout(request)
        context = {
                "title": "Anmeldung Punktestand CHE119",
                "range": range(1,9),
            }
        return render(request, "score/login.html", context=context)

def detail(request, exam_number):
    if request.user.is_authenticated:
        student = list(Student.objects.filter(student_user=request.user))[0]
        exams = WrittenExam.objects.filter(student=student)
        exam_numbers = [str(exam.exam_number) for exam in exams]
        exam = [exam for exam in exams][0]
        participation = list(Participation.objects.filter(student=student))[0]

        context = {
            "participation": participation,
            "range": range(1,9),
            "student": student,
            "exam": exam,
            "exam_number": str(exam_number),
            "exams": exams,
            "exam_numbers": exam_numbers,
            "immatriculation_number": str(student.immatriculation_number),
            "title": "CHE119 Beurteilungen SS2024"
        }
        return render(request, "score/detail.html", context=context)
