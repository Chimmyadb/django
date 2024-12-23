from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    address=models.TextField()
    contact_no=models.CharField(max_length=10, unique=True)
    guardian_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Class(models.Model):
    class_id=models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=40)
    teacher_name=models.CharField(max_length=50)

    def __str__(self):
        return self.class_name
    
class Attendence(models.Model):
    attendence_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=10, choices=[('Present','Present'),('Absent','Absent')])

    def __str__(self):
        return f"{self.student.name} -{self.date}"

class Grade(models.Model):
    grade_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    marks=models.IntegerField()
    term=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.student.name}-{self.subject}"


        

