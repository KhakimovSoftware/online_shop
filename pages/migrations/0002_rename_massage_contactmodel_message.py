# Generated by Django 4.0.6 on 2022-07-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='massage',
            new_name='message',
        ),
    ]
