# Generated by Django 2.0 on 2017-12-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(choices=[(0, 'admin'), (1, 'student'), (2, 'teacher')], default=1),
        ),
        migrations.AlterField(
            model_name='temporarypassword',
            name='level',
            field=models.IntegerField(choices=[(0, 'admin'), (1, 'student'), (2, 'teacher')]),
        ),
    ]
