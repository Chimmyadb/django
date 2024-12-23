from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from students.views import*


router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('classes', ClassViewSet)
router.register('attendence', AttendenceViewSet)
router.register('grades', GradeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),   
    # path('api/', include('students.urls')),

]
