# Generated by Django 4.1.7 on 2023-04-25 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_paleta_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paleta',
            old_name='modelo',
            new_name='tipo',
        ),
    ]
