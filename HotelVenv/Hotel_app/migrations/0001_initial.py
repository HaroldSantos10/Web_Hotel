# Generated by Django 4.1.2 on 2022-11-05 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblcliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default='0')),
                ('identificacion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='tblhabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_habitacion', models.CharField(max_length=5)),
                ('piso', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('disponibilidad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tblhotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblciudad')),
            ],
        ),
        migrations.CreateModel(
            name='tblpais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblprecio_habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='tbltemporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_temp', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='tbltipo_habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_habitacion', models.CharField(max_length=200)),
                ('cant_camas', models.IntegerField()),
                ('vista', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tbltipo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_pago', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbltipo_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_servicio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
                ('tipo_servicio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_servicio')),
            ],
        ),
        migrations.CreateModel(
            name='tblreservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_dias', models.IntegerField()),
                ('fecha_registro', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblcliente')),
                ('habitacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhabitacion')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhotel')),
                ('precio_hab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblprecio_habitacion')),
            ],
        ),
        migrations.AddField(
            model_name='tblprecio_habitacion',
            name='temporda_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltemporada'),
        ),
        migrations.AddField(
            model_name='tblprecio_habitacion',
            name='tipo_habitacion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_habitacion'),
        ),
        migrations.CreateModel(
            name='tblpago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reservacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblreservacion')),
                ('servicio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblservicio')),
                ('tipo_pago_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_pago')),
            ],
        ),
        migrations.AddField(
            model_name='tblhotel',
            name='pais_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblpais'),
        ),
        migrations.AddField(
            model_name='tblhabitacion',
            name='hotel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhotel'),
        ),
        migrations.AddField(
            model_name='tblhabitacion',
            name='tipo_habitacion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_habitacion'),
        ),
        migrations.AddField(
            model_name='tblcliente',
            name='habitacion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhabitacion'),
        ),
    ]
