# from django.urls import path
# from students import views
# # from django.conf import settings

# urlpatterns=[
#     path('/',)
# ]

from django.urls import path,include
from .views import StudentDetailView
from students.views import SecondaryStudentList


urlpatterns = [
    path('students/<int:id>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/', SecondaryStudentList.as_view(), name='create-secondary-student'),
    # path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
