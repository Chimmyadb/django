from django.shortcuts import render
from rest_framework import viewsets
from .models import*
from .serializers import*
from rest_framework.decorators import api_view #permission_classes
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views import View
import json
from rest_framework.views import APIView





class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer

class AttendenceViewSet(viewsets.ModelViewSet):
    queryset=Attendence.objects.all()
    serializer_class=AttendenceSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset=Grade.objects.all()
    serializer_class=GradeSerializer
    



class SecondaryStudentList(APIView):
    """
    API to create a new secondary student record.
    """
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SecondaryStudentDetail(APIView):
    """
    API to update or create a single secondary student record by ID.
    """
    def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            # If the student does not exist, create a new one
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentDetailView(View):
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
            data = json.loads(request.body)

            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            student.grade = data.get("grade", student.grade)
            student.address = data.get("address", student.address)
            student.save()

            return JsonResponse({"message": "Student updated successfully"}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"message": "Student deleted successfully"}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)


