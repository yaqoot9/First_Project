# Generated by Django 4.1.1 on 2022-09-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(choices=[('Fmale', 'F'), ('Male', 'm')], max_length=10),
        ),
    ]
