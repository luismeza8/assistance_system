# Generated by Django 5.0.4 on 2024-07-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_register_delete_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='check_in_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='check_out_time',
            field=models.TimeField(auto_now=True),
        ),
    ]