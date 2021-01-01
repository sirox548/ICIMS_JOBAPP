from django.db import models


class Employer(models.Model):
    job_choices = (("Part Time", "part time"),
                   ("Full Time", "full time"),
                   ("Internship", "internship"),
                   ("Contract", "contract"),
                   ("Temporary", "temporary"))
    exp_choices = (("No Experience", "no experience"),
                   ("Intermediate", "intermediate"),
                   ("Advance", "advance"),
                   ("Expertise", "expertise"))
    job_title = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=100, choices=job_choices)
    salary = models.IntegerField(max_length=14, null=True)
    description = models.TextField(max_length=500, null=True)
    required_skills = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    years_of_experience = models.CharField(max_length=50, choices=exp_choices)
    education = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.job_title
