# Generated by Django 2.2.5 on 2019-11-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0017_admin_brochure'),
    ]

    operations = [
        migrations.DeleteModel(
            name='department',
        ),
        migrations.AlterField(
            model_name='admin',
            name='brochure',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='admin',
            name='ddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='department',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='admin',
            name='descreption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='eventname',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='admin',
            name='regfee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='tpm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='venue',
            field=models.TextField(),
        ),
    ]