from django.urls import path
from .views import *
urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('admin-profile/', AdminProfile.as_view(), name='admin-profile'),
    path('pupil-profile/', PupilProfile.as_view(), name='pupil-profile'),
    path('teacher-profile/', TeacherProfile.as_view(), name='teacher-profile'),
    path('pupils/', PupilList.as_view(), name='pupils'),
    path('teachers/', TeacherList.as_view(), name='teachers'),
    path('users/', UserList.as_view(), name='users'),

]
