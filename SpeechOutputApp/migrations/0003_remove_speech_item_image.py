# Generated by Django 2.2 on 2021-04-11 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpeechOutputApp', '0002_speech_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speech_item',
            name='image',
        ),
    ]