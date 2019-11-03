# Generated by Django 2.2.5 on 2019-11-03 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0011_auto_20191103_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='user2',
            name='eventid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventApp.User', to_field='username'),
        ),
    ]
