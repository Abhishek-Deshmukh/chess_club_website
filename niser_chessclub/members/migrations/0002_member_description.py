# Generated by Django 2.2 on 2019-06-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.CharField(default=' ', max_length=10000),
        ),
    ]
