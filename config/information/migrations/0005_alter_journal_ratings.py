# Generated by Django 4.0.5 on 2022-06-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_alter_journal_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='ratings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
