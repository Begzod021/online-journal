# Generated by Django 4.0.5 on 2022-06-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_is_pupil'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_pupil',
            field=models.BooleanField(default=False),
        ),
    ]
