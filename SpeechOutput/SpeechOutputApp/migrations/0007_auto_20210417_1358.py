# Generated by Django 2.2 on 2021-04-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpeechOutputApp', '0006_auto_20210411_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
