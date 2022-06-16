from logging import error
from re import sub
from .serializers import JournalSerializer, ClassNumSerializer
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from users.api.serializers import (
    PupilSerializer,
    TeacherSerializer,
    UserSerializer
)
from users.models import (
    Teacher,
    Pupil
)
from information.models import Journal, ClassNum
from users.api.permissions import (
    IsParent,
    IsPupil,
    IsTeacher,
    IsAdminOrReadOnly,
    IsAuthenticated,
    IsAdminOrIsTeacher

)
from rest_framework import status

class JournalPostRetings(APIView):
    permission_classes = [IsTeacher]
    def post(self, request):

        teacher_id = request.user
        seriazlier = JournalSerializer(data=request.data)

        if seriazlier.is_valid(raise_exception=True):


            sub_teacher = seriazlier.validated_data["subject"]
            class_number = seriazlier.validated_data["class_number"]
            pupil = seriazlier.validated_data["pupil"]


            if sub_teacher.teacher == teacher_id and pupil.class_number == class_number:
                    seriazlier.save(teacher = request.user)
                    return Response(seriazlier.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class JournalList(APIView):
    permission_classes = [IsAdminOrIsTeacher]

    def get(self, request):
        journals = Journal.objects.all()

        serializer = JournalSerializer(journals, many=True)

        return Response(serializer.data)


class JournalForPupilDetailView(APIView):
    permission_classes = [IsPupil]
    def get(self, reqeust):
        journal = Journal.objects.filter(pupil = reqeust.user)
        serializer = JournalSerializer(journal, many=True)

        return  Response(serializer.data, status=status.HTTP_200_OK)

class JournalForTeacherAdminDetailView(APIView):
    permission_classes = [IsAdminOrIsTeacher]

    def get(self, request, pk):
        
        journal = Journal.objects.get(id = pk)
        serializer = JournalSerializer(journal, many=False)

        return  Response(serializer.data, status=status.HTTP_200_OK)


class JournalPatch(APIView):
    permission_classes = [IsTeacher]

    def patch(self, request, pk):

        journal = Journal.objects.get(id = pk)
        serializer = JournalSerializer(journal, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(teacher = request.user)

            return  Response(serializer.data, status=status.HTTP_200_OK)

class JournalFilterTeacher(APIView):
    permission_classes = [IsTeacher]

    def get(self, request):

        journal = Journal.objects.filter(teacher = request.user)
        serializer = JournalSerializer(journal, many=True)

        return  Response(serializer.data, status=status.HTTP_200_OK)
