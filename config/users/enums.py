from enum import Enum

class UserRole(Enum):
    teacher = 'teacher'
    pupil = 'pupil'
    parent = 'parent'
    admin = 'admin'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)