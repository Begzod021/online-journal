# Generated by Django 4.0.5 on 2022-06-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0006_alter_journal_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='ratings',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]