from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from student_class.models import Student_Class
from teacher.models import Teacher
from course.models import Course
from classperiod.models import Class_Period
from api.serializer import StudentSerializer, Student_ClassSerializer, TeacherSerializer, CourseSerializer, Class_PeriodSerializer

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many =True)
        return Response(serializer.data)
    
class Student_ClassListView(APIView):
    def get(self, request):
        student_classes = Student_Class.objects.all()
        serializer = Student_ClassSerializer(student_classes, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
 
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
class Class_PeriodListView(APIView):
    def get(self, request):
        class_periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_periods, many=True)
        return Response(serializer.data)