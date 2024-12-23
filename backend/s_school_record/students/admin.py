from django.contrib import admin

# Register your models here.
from .models import Student,Class,Attendence, Grade
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Attendence)
admin.site.register(Grade)
