# Generated by Django 2.0.3 on 2019-10-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist', models.CharField(max_length=50)),
                ('artist_location', models.CharField(blank=True, max_length=50, null=True)),
                ('artist_bio', models.TextField(blank=True, null=True)),
                ('artist_nice_name', models.CharField(blank=True, max_length=50, null=True)),
                ('artist_type', models.CharField(max_length=20)),
                ('artist_contact', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=12)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='ArtistLink',
            fields=[
                ('artist_nice_name', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=240, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'artist_links',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('row', models.CharField(max_length=3)),
                ('cat_num', models.CharField(max_length=6)),
                ('fk_artist', models.CharField(blank=True, max_length=50)),
                ('release_title', models.CharField(blank=True, max_length=80, null=True)),
                ('release_formats', models.CharField(blank=True, max_length=24, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('artist_nice_name', models.CharField(max_length=50)),
                ('tracklisting', models.TextField()),
                ('bio', models.TextField()),
                ('ffo', models.TextField()),
                ('target_markets', models.TextField()),
                ('upc', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=20)),
                ('mediaplayer_html', models.TextField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'releases',
            },
        ),
        migrations.CreateModel(
            name='ReleaseLink',
            fields=[
                ('cat_num', models.CharField(blank=True, max_length=6, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=240, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'release_links',
            },
        ),
    ]
