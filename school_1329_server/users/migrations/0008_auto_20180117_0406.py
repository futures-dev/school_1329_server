# Generated by Django 2.0 on 2018-01-17 01:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180116_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationcode',
            name='code',
            field=models.CharField(default='pnCHZ90Q', max_length=32),
        ),
        migrations.AlterField(
            model_name='registrationcode',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 24, 1, 5, 59, 923401, tzinfo=utc)),
        ),
    ]
