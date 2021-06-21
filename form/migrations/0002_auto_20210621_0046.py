# Generated by Django 3.1.3 on 2021-06-20 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='phone_no',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='studentform',
            name='reg_no',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='studentform',
            name='sex',
            field=models.CharField(choices=[('CS', 'Choose sex'), ('M', 'male'), ('F', 'female')], default='CS', max_length=10),
        ),
    ]
