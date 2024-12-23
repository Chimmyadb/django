from rest_framework import serializers
from .models import*

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','age','gender','address','contact_no','guardian_name']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields='__all__'

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendence
        fields='__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grade
        fields='__all__'