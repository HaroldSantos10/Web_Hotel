# Generated by Django 4.1.3 on 2022-11-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_app', '0004_remove_tblreservacion_habitacion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblreservacion',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='tblreservacion',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
