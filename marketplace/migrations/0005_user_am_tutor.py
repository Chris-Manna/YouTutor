# Generated by Django 2.1.7 on 2020-11-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_user_tutor_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='am_tutor',
            field=models.BooleanField(default=True),
        ),
    ]
