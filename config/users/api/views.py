from datetime import datetime
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsAdminOrReadOnly, IsParent, IsPupil, IsTeacher, TeacherUpdatePermission
from .serializers import (
    UserSerializerWithToken,
    UserRegisterSerializer,
    UserSerializer,
    TeacherSerializer,
    PupilSerializer,
    PupilProfileSerializer,
    TeacherProfileSerializer,
)
from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import *
from information.models import Journal
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from users.models import User






class UserRegister(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        user = UserRegisterSerializer(data=request.data)
        if user.is_valid(raise_exception=True):
            user.save()
            return Response(user.data, status=status.HTTP_200_OK)
        
        return Response(user.data, status=status.HTTP_502_BAD_GATEWAY)

class AdminProfile(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        serializer = UserSerializer(request.user, many=False)

        return Response(serializer.data)


class PupilProfile(APIView):
    permission_classes = [IsPupil]

    def get(self, request):

        pupil = Pupil.objects.get(id = request.user.id)
        serializer = PupilProfileSerializer(pupil, many=False)

        return Response(serializer.data)

    def patch(self, request):

        pupil = Pupil.objects.get(id = request.user.id)
        seriazlier = PupilProfileSerializer(pupil, many=False, data=request.data)

        if seriazlier.is_valid():
            seriazlier.save()

            return Response(seriazlier.data, status=status.HTTP_200_OK)

        return Response(seriazlier.data, status=status.HTTP_502_BAD_GATEWAY)




class TeacherProfile(APIView):
    permission_classes = [IsTeacher]
    def get(self, request):

        teacher = Teacher.objects.get(id = request.user.id)
        serializer = TeacherProfileSerializer(teacher, many=False)

        return Response(serializer.data)

    def patch(self, request):

        teacher = Teacher.objects.get(id = request.user.id)
        serializer = TeacherProfileSerializer(teacher, data=request.data)


        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.data, status=status.HTTP_502_BAD_GATEWAY)




class PupilList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        pupils = Pupil.objects.all()
        serializer = PupilSerializer(pupils, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class TeacherList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




class UserList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        for i in serializer.data:

            if i["role"] != "pupil":

                del i["class_number"]

        return Response(serializer.data, status=status.HTTP_200_OK)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        self.user.last_login = datetime.now()
        self.user.save()

        if self.user.role != "pupil":

            del serializer["class_number"]
            
        for key, val in serializer.items():
            data[key] = val

        return data



class MyTokenObtainPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer  