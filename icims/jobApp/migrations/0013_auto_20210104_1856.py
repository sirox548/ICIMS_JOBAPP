# Generated by Django 3.1.4 on 2021-01-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0012_auto_20210104_1328'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddSkills',
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='address_option',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='joiner',
        ),
        migrations.AddField(
            model_name='candidate',
            name='skill',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employer',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Joiner',
        ),
    ]
