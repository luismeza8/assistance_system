# Generated by Django 5.0.4 on 2024-06-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_miembro_groups_miembro_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]
