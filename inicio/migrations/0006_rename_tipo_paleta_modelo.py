# Generated by Django 4.1.7 on 2023-04-25 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_rename_modelo_paleta_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paleta',
            old_name='tipo',
            new_name='modelo',
        ),
    ]
