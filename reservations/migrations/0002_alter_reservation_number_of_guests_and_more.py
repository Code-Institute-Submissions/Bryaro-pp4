# Generated by Django 4.2.9 on 2024-02-09 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_of_guests',
            field=models.IntegerField(choices=[(1, '1 guest'), (2, '2 guests'), (3, '3 guests'), (4, '4 guests'), (5, '5 guests'), (6, '6 guests'), (7, '7 guests'), (8, '8 guests')]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(choices=[(datetime.time(7, 0), '7:00 AM'), (datetime.time(9, 0), '9:00 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(13, 0), '1:00 PM'), (datetime.time(15, 0), '3:00 PM'), (datetime.time(17, 0), '5:00 PM'), (datetime.time(19, 0), '7:00 PM'), (datetime.time(21, 0), '9:00 PM')]),
        ),
    ]
