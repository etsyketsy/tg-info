# Generated by Django 2.0.3 on 2019-10-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_artistlink_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='artist',
            field=models.ManyToManyField(blank=True, related_name='releases', to='api.Artist'),
        ),
        migrations.AddField(
            model_name='releaselink',
            name='release',
            field=models.ManyToManyField(blank=True, related_name='links', to='api.Release'),
        ),
        migrations.AlterField(
            model_name='artistlink',
            name='artist',
            field=models.ManyToManyField(blank=True, related_name='links', to='api.Artist'),
        ),
    ]
