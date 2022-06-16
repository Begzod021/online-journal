# Generated by Django 4.0.5 on 2022-06-11 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.manager
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
        ('users', '0008_delete_classnumber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pupil',
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('class_numbers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='information.classnum')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=(users.models.Model, 'users.user'),
            managers=[
                ('objects', users.manager.PupilManager()),
            ],
        ),
    ]