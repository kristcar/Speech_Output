# Generated by Django 2.2 on 2021-04-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpeechOutputApp', '0007_auto_20210417_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]