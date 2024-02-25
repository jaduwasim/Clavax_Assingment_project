from rest_framework.viewsets import ModelViewSet
from student.models import StudentUser
from student.api.serializers import StudentUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentUserCBV(ModelViewSet):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]