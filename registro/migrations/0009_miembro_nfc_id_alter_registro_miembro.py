# Generated by Django 5.0.4 on 2024-05-08 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_alter_miembro_options_alter_miembro_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='nfc_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='registro',
            name='miembro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.miembro'),
        ),
    ]
