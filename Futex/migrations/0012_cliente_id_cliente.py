# Generated by Django 4.0.6 on 2022-07-20 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Futex', '0011_alter_cliente_email_alter_time_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='id_cliente',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]