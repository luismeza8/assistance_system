# Generated by Django 5.0.4 on 2024-04-30 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_alter_miembro_options_alter_miembro_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miembro',
            options={},
        ),
        migrations.AlterModelManagers(
            name='miembro',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='email',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='password',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='username',
        ),
        migrations.AlterField(
            model_name='miembro',
            name='mision',
            field=models.ManyToManyField(to='registro.mision'),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='subsistema',
            field=models.ManyToManyField(to='registro.subsistema'),
        ),
    ]
