from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=28)
    gender = models.CharField(max_length=10, default='Unknown')
    bio = models.TextField(null=True, blank=True)
    enrollment_date = models.DateField(default='2024-01-01')
    class_name = models.CharField(max_length=30, default='Unknown')
    grade_level = models.IntegerField(default='Unkown')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"