from rest_framework import serializers
from student.models import Student
from student_class.models import Student_Class
from teacher.models import Teacher
from course.models import Course
from classperiod.models import Class_Period

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class Student_ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Class
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'