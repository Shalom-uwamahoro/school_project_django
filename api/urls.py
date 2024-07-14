from django.urls import path

from .views import StudentListView, Student_ClassListView, TeacherListView, CourseListView, Class_PeriodListView


urlpatterns = [
    path('students/', StudentListView.as_view(), name ="student_list_view"),
    path('student_classes/', Student_ClassListView.as_view(),name = "student_class_list_view"),
    path('teachers/', TeacherListView.as_view(),name = "teacher_list_view"),
    path('courses/', CourseListView.as_view(),name = "course_list_view"),
    path('class_periods/', Class_PeriodListView.as_view(),name = "class_period_list_view")

]


  
