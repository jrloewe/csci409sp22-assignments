# Generated by Django 4.1.5 on 2023-02-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airports', '0002_runway'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=255)),
                ('airline_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('aircraft_type', models.CharField(max_length=10)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.airline')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_destination', to='airports.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_origin', to='airports.airport')),
            ],
        ),
    ]
