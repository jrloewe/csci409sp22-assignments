# Generated by Django 4.1.5 on 2023-02-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]