# Generated by Django 2.1.2 on 2018-11-25 13:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0009_auto_20181125_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Staff',
            new_name='Staff_name',
        ),
        migrations.AlterField(
            model_name='employee',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 11, 25, 13, 6, 6, 217616, tzinfo=utc)),
        ),
    ]
