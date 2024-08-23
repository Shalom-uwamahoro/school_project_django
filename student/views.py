from django.shortcuts import render


from .forms import StudentRegistrationFrom

def register_student(request):
    form = StudentRegistrationFrom()
    return render(request, "student/register_student.html", {"form":form})