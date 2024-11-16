from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views
from .views import StudentWorkViewSet

router = DefaultRouter()
router.register(r'student-work', StudentWorkViewSet, basename='student_work')

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', include(router.urls)),
]