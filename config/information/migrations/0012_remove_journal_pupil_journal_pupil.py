# Generated by Django 4.0.5 on 2022-06-11 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_class_number'),
        ('information', '0011_remove_journal_pupil_journal_pupil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='pupil',
        ),
        migrations.AddField(
            model_name='journal',
            name='pupil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pupils', to='users.pupil'),
        ),
    ]
