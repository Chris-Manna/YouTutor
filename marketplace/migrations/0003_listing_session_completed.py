# Generated by Django 2.1.7 on 2020-12-03 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_user_wonlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='session_completed',
            field=models.BooleanField(default=False),
        ),
    ]
