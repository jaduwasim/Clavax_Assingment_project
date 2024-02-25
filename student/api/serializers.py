from rest_framework import serializers
from student.models import StudentUser

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['first_name','last_name','email','image','date_of_birth','phone','class_name']
