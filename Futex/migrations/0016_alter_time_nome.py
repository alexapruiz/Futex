# Generated by Django 4.0.6 on 2022-07-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0015_alter_time_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='nome',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
