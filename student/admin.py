from django.contrib import admin
from .models import StudentUser

# Register your models here.

@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','date_of_birth','phone','image', 'class_name','status']