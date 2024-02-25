from django.urls import path, include
from student.api.views import StudentUserCBV
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()
router.register('api', StudentUserCBV, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('get-token/',TokenObtainPairView.as_view()),
]