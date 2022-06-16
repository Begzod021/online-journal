from django.db import models

# Create your models here.

class ClassNum(models.Model):
    class_num = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.class_num

class Subjects(models.Model):
    choices = (
        ('',''),
        ('Ona Tili','Ona Tili'),
        ('Adabiyot','Adabiyot'),
        ('Matematika','Matematika'),
        ('Ingliz Tili','Ingliz Tili'),
        ('Odobnoma','Odobnoma'),
        ('Jahon Tarix', 'Jahon Tarix'),
        ('O`zbekiston Tarix', 'O`zbekiston Tarix'),
        ('Musiqa','Musiqa'),
    )
    subjects = models.CharField(max_length=33, choices=choices)
    teacher = models.ForeignKey('users.Teacher', on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return self.subjects

class Journal(models.Model):
    class_number = models.ForeignKey(ClassNum, on_delete=models.PROTECT, blank=True, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    ratings = models.PositiveIntegerField(blank=True, null=True)
    teacher = models.ForeignKey("users.Teacher", on_delete=models.PROTECT, blank=True, null=True)
    nb = models.BooleanField(default=False)
    pupil = models.ForeignKey("users.Pupil",on_delete=models.CASCADE, related_name="pupils", blank=True, null=True)
    def __str__(self):
        return str(self.subject)

