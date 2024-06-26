# Generated by Django 5.0.4 on 2024-06-06 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('registro', '0009_miembro_nfc_id_alter_registro_miembro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miembro',
            name='mision',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='subsistema',
        ),
        migrations.AlterField(
            model_name='registro',
            name='miembro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.miembro'),
        ),
        migrations.RemoveField(
            model_name='subsistema',
            name='lider',
        ),
        migrations.DeleteModel(
            name='Mision',
        ),
        migrations.DeleteModel(
            name='Miembro',
        ),
        migrations.DeleteModel(
            name='Subsistema',
        ),
    ]
