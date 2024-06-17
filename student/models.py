from django.db import models
# Create your models here.

class Student(models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    country= models.CharField(max_length=20)
    date_of_birth=models.DateField()
    code= models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f" {self.first_name} {self.last_name}"

# class Student(models.Model):   # we are inheriting the mode becase it hall all we need
#     first_name = models.CharField(max_length = 20)
#     last_name = models.CharField(max_length = 20)
#     id = models.AutoField()
#     gender = models.CharField(max_length = 7)
#     email= models.EmailField()
#     date_of_birth = models.DateField()
#     code = models.PositiveBigIntegerField()
#     country = models.CharField(max_length = 28)
#     bio= models.TextField()
#     enrollment_date = models.DateField()
#     class_id =models.IntegerField()
#     grade_level = models.IntegerField()

# class Teacher(models.Model):   
#     first_name = models.CharField(max_length = 20)
#     last_name = models.CharField(max_length = 20)
#     id = models.IntegerField()
#     gender = models.CharField(max_length = 7)
#     email= models.EmailField()
#     date_of_birth = models.DateField()
#     code = models.PositiveBigIntegerField()
#     country = models.CharField(max_length = 28)
#     bio= models.TextField()
#     education_level = models.CharField()
#     course_id = models.IntegerField()
#     class_id = models.ForeignKey()
#     subject_specialisation = models.CharField()
#     phone_number = models.CharField()

# class Course(models.Model):   
#     id = models.IntegerField()
#     course_name = models.CharField()
#     course_department = models.CharField()
#     course_prequisites = models.TextField()
#     course_description = models.TextField()
#     teacher_id = models.ForeignKey()
#     created_at = models.DateTimeField()
#     trimester = models.PositiveBigIntegerField()
#     course_head = models.CharField()
#     enrollment_limit = models.IntegerField()
#     class_id = models.ForeignKey() 

# class Class(models.Model):   
#     id = models.AutoField()
#     class_name = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     teacher_id = models.ForeignKey()
#     class_decription = models.TextField()
#     school_year = models.IntegerField()
#     capacity = models.IntegerField()
#     room_number = models.IntegerField()
#     grade_level = models.IntegerField()









   




    


       