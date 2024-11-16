from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('student-work/', StudentWorkView.as_view(), name='student-work-list'),
    path('student-work/', views.student_work_upload, name='student_work_upload'),
    path('api/student-works/<str:username>/', views.get_student_works, name='get_student_works'),
]