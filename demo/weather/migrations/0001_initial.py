# Generated by Django 4.0.3 on 2022-03-27 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('longitude', models.FloatField()),
                ('lattitude', models.FloatField()),
                ('grid_i', models.IntegerField()),
                ('grid_j', models.IntegerField()),
                ('grid_height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('parameter', models.TextField(primary_key=True, serialize=False)),
                ('unit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('member', models.IntegerField()),
                ('leadtime', models.TextField()),
                ('value', models.FloatField(default=-999.0)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station', to='weather.station')),
                ('weather_param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather_param', to='weather.unit')),
            ],
        ),
    ]
