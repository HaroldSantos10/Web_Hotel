# Generated by Django 4.1.3 on 2022-11-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_app', '0002_remove_tblcliente_reservacion_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblsuscripciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]