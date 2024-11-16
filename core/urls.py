from django.urls import path, include

from . import views
from .views import StudentWorkView


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('student-work/', StudentWorkView.as_view(), name='student-work-list'),
]