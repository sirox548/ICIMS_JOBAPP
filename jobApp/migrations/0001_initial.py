# Generated by Django 3.1.4 on 2021-01-01 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('job_type', models.CharField(choices=[('Part Time', 'part time'), ('Full Time', 'full time'), ('Internship', 'internship'), ('Contract', 'contract'), ('Temporary', 'temporary')], max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('years_of_experience', models.CharField(choices=[('No Experience', 'no experience'), ('Intermediate', 'intermediate'), ('Advance', 'advance'), ('Expertise', 'expertise')], max_length=50)),
            ],
        ),
    ]
