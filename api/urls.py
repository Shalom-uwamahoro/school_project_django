from django.urls import path

from .views import StudentListView, Student_ClassListView, TeacherListView, CourseListView, Class_PeriodListView, StudentDetailView, Student_ClassDetailView, TeacherDetailView, CourseDetailView, Class_PeriodDetailView


urlpatterns = [
    path('students/', StudentListView.as_view(), name ="student_list_view"),
    # path('students/', MinimalStudentSerializer.as_view(), name ="student_minimal_view"),

    
    path('student_classes/', Student_ClassListView.as_view(),name = "student_class_list_view"),
    path('teachers/', TeacherListView.as_view(),name = "teacher_list_view"),
    path('courses/', CourseListView.as_view(),name = "course_list_view"),
    path('class_periods/', Class_PeriodListView.as_view(),name = "class_period_list_view"),

    path('students/<int:id>/', StudentDetailView.as_view()),
    path('student_classes/<int:id>/', Student_ClassDetailView.as_view()),
    path('teachers/<int:id>/', TeacherDetailView.as_view()),
    path('courses/<int:id>/', CourseDetailView.as_view()),
    path('class_periods/<int:id>/', Class_PeriodDetailView.as_view())

]


  
