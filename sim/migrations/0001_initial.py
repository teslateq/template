# Generated by Django 2.1.3 on 2018-11-03 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.BooleanField()),
                ('r2', models.BooleanField()),
                ('r3', models.BooleanField()),
                ('r4', models.BooleanField()),
                ('s1', models.BooleanField()),
                ('s2', models.BooleanField()),
                ('s3', models.BooleanField()),
                ('s4', models.BooleanField()),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyRest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr', models.IntegerField()),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GPRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gprs', models.IntegerField()),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modbus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baud_master', models.CharField(choices=[('0', '4800'), ('1', '9600'), ('2', '14400'), ('3', '19200'), ('4', '28800'), ('5', '38400'), ('6', '56000'), ('7', '57600'), ('8', '115200'), ('9', '128000'), ('A', '256000')], default='9', max_length=1)),
                ('address_master', models.CharField(max_length=2)),
                ('baud_slave', models.CharField(choices=[('0', '4800'), ('1', '9600'), ('2', '14400'), ('3', '19200'), ('4', '28800'), ('5', '38400'), ('6', '56000'), ('7', '57600'), ('8', '115200'), ('9', '128000'), ('A', '256000')], default='9', max_length=1)),
                ('address_slave', models.CharField(max_length=2)),
                ('address_resgiter_master', models.CharField(max_length=4)),
                ('length_resgiter_master', models.CharField(max_length=4)),
                ('upd', models.BooleanField(default=0)),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('symbol_name', models.CharField(max_length=20)),
                ('start_address', models.IntegerField()),
                ('type', models.CharField(choices=[('2', 'Int'), ('4', 'Float')], default='2', max_length=1)),
                ('scale', models.FloatField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('symbol_name', models.CharField(max_length=50)),
                ('serial', models.IntegerField()),
                ('managed_by_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StationConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=20)),
                ('symbol_name', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station')),
            ],
        ),
        migrations.CreateModel(
            name='StationConfigValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
                ('station_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.StationConfig')),
            ],
        ),
        migrations.CreateModel(
            name='StationHealthy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=20)),
                ('symbol_name', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station')),
            ],
        ),
        migrations.CreateModel(
            name='StationHealthyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
                ('station_healthy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.StationHealthy')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sig', models.IntegerField()),
                ('temp', models.FloatField()),
                ('vol', models.FloatField()),
                ('cnn', models.BooleanField()),
                ('b', models.IntegerField()),
                ('n', models.BooleanField()),
                ('d', models.BooleanField()),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=255)),
                ('ngaygio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='parameter',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station'),
        ),
        migrations.AddField(
            model_name='modbus',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station'),
        ),
        migrations.AddField(
            model_name='gprs',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station'),
        ),
        migrations.AddField(
            model_name='dailyrest',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station'),
        ),
        migrations.AddField(
            model_name='control',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Station'),
        ),
    ]
