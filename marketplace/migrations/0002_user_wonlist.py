# Generated by Django 2.1.7 on 2020-12-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wonlist',
            field=models.ManyToManyField(blank=True, related_name='winners', to='marketplace.Listing'),
        ),
    ]
