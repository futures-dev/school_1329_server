# Generated by Django 2.0 on 2018-02-03 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20180204_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulelesson',
            name='place',
            field=models.CharField(default='Москва', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedulelesson',
            name='groups',
            field=models.ManyToManyField(blank=True, to='groups.Group'),
        ),
    ]