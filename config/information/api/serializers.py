from rest_framework import serializers
from information.models import Journal, ClassNum, Subjects
from users.models import *


class ListPupil(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = ["username", "role"]

class ClassNumSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassNum
        fields = ["class_num"]


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects

        fields = "__all__"


class JournalSerializer(serializers.ModelSerializer):
    class_number = serializers.SerializerMethodField(read_only = True)
    subject = serializers.SerializerMethodField(read_only = True)
    pupil = serializers.SerializerMethodField(read_only = True )

    class Meta:
        model = Journal
        fields = ["id", "class_number", "subject", "ratings", "teacher", "pupil"]

    def get_class_number(self, obj):
        class_number = obj.class_number
        serializer = ClassNumSerializer(class_number, many = False)

        return serializer.data

    def get_subject(self, obj):
        subject = obj.subject

        serializer = SubjectSerializer(subject, many = False)

        return serializer.data


    def get_pupil(self, obj):

        teacher = obj.pupil

        serializer = ListPupil(teacher, many = False)

        return serializer.data

    


