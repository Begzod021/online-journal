# Generated by Django 4.0.5 on 2022-06-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_class_number'),
        ('information', '0010_remove_journal_pupil_journal_pupil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='pupil',
        ),
        migrations.AddField(
            model_name='journal',
            name='pupil',
            field=models.ManyToManyField(blank=True, null=True, related_name='pupils', to='users.pupil'),
        ),
    ]
