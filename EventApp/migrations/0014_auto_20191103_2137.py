# Generated by Django 2.2.5 on 2019-11-03 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0013_auto_20191103_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user2',
            old_name='username',
            new_name='username2',
        ),
    ]
