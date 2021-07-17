# Generated by Django 2.1.3 on 2018-12-09 11:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0014_auto_20181208_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'get_latest_by': ['time']},
        ),
        migrations.AlterField(
            model_name='employee',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 12, 9, 11, 3, 50, 700876, tzinfo=utc)),
        ),
    ]
