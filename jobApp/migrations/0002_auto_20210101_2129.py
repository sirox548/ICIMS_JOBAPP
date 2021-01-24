# Generated by Django 3.1.4 on 2021-01-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='education',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employer',
            name='required_skills',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employer',
            name='salary',
            field=models.IntegerField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='job_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]