# Generated by Django 4.2.2 on 2023-09-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_song_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='избранное'),
        ),
    ]