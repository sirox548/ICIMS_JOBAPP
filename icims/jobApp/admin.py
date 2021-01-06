from django.contrib import admin
from .models import Employer, Candidate, Joiner, Jobs

admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(Joiner)
admin.site.register(Jobs)

