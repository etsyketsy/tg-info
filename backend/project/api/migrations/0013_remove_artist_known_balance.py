# Generated by Django 2.2.4 on 2019-08-23 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190821_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='known_balance',
        ),
    ]