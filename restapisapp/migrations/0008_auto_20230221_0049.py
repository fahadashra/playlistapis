# Generated by Django 3.2.17 on 2023-02-21 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapisapp', '0007_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='album',
            new_name='playlist_name',
        ),
        migrations.RenameField(
            model_name='playlist',
            old_name='artist',
            new_name='songname',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='title',
        ),
    ]
