# Generated by Django 3.0.2 on 2020-01-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_with',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
