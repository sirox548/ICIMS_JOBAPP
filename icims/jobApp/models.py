from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    high_light = models.CharField(max_length=200, null=True)
    skill = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    volunteer = models.CharField(max_length=100, null=True)
    hobbies = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "%s %s"%(self.name, self.high_light)


class Joiner(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


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
    company = models.CharField(max_length=100, null=True)
    job_title = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=100, choices=job_choices)
    salary = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    description = models.TextField(max_length=500, null=True)
    required_skills = models.TextField(max_length=900, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    years_of_experience = models.CharField(max_length=50, choices=exp_choices)
    education = models.CharField(max_length=200, null=True)
    schedule = models.CharField(max_length=100, null=True)
    benefits = models.TextField(max_length=100, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    join = models.ManyToManyField(Joiner)

    def __str__(self):
        return "%s   %s"%(self.company, self.job_title)


class Jobs(models.Model):
    app_status = (('Resume Review', 'resume review'),
                  ('Interview Process', 'Interview Process'),
                  ('Offer Submitted', 'offer submitted'),
                  ('Hired', 'hired'))
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, null=True, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=app_status)
    feedback = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.candidate.name