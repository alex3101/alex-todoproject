# Generated by Django 3.0.6 on 2020-06-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_profileupdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileUpdate',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]