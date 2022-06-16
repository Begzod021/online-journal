from urllib import request
from django.db.models import manager
from django.contrib.auth.models import UserManager
from information.models import ClassNum
class TeacherManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="teacher")


class PupilManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="pupil")


class ParentManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="parent")


class AdminManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="admin", is_staff=True)