# Generated by Django 4.1.7 on 2023-04-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_delete_paleta_rename_marca_gasto_articulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='gastos/'),
        ),
    ]
