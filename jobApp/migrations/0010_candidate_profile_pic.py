# Generated by Django 3.1.4 on 2021-01-04 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0009_candidate_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
