# Generated by Django 5.0.6 on 2024-05-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
