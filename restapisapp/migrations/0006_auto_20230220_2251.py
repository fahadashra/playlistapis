# Generated by Django 3.2.17 on 2023-02-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapisapp', '0005_auto_20230215_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlistsong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('album', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
