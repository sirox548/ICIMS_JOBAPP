# Generated by Django 3.1.4 on 2021-01-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0011_auto_20210104_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addskills',
            name='joiner',
        ),
        migrations.AddField(
            model_name='employer',
            name='joiner',
            field=models.ManyToManyField(to='jobApp.Joiner'),
        ),
    ]
