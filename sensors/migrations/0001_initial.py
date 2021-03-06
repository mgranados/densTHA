# Generated by Django 3.2.5 on 2021-07-20 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50)),
                ('uuid', models.UUIDField()),
                ('online', models.BooleanField(default=False)),
                ('metadata', models.JSONField()),
                ('created_at', models.DateField(auto_now=True)),
                ('last_heartbeat_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Heartbeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor')),
            ],
        ),
    ]
