from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import *
from .manager import *
from information.models import *
# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=UserRole.choices())
    approve = models.BooleanField(default=False)
    class_number = models.ForeignKey(ClassNum, on_delete=models.PROTECT, blank=True, null=True)


class Teacher(User):
    objects = TeacherManager()
    
    class Meta:
        proxy = True


class Model(object):
    '''
    Skip extra field validation "models.E017"
    '''

    @classmethod
    def _check_model(cls):
        errors = []
        return errors

class Pupil(Model,User):
    objects = PupilManager()


    class Meta:
        proxy = True
class Parent(User):
    objects = ParentManager()

    class Meta:
        proxy = True


class Admin(User):

    objects = AdminManager()

    class Meta:
        proxy = True

    


