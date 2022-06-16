# Generated by Django 4.0.5 on 2022-06-11 21:16

from django.db import migrations
import users.manager
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_delete_pupil_pupil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pupil',
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=(users.models.Model, 'users.user'),
            managers=[
                ('objects', users.manager.PupilManager()),
            ],
        ),
    ]
