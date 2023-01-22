from django.db import models

# Create your models here.
class Profile(models.Model):
    """This class creates objects that can be used to fill out the CV form for each user."""
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=8)
    email = models.EmailField(max_length=150)
    secondary_education = models.CharField(max_length=150)
    tertiary_education = models.CharField(max_length=150)
    degree_name = models.CharField(max_length=150)
    skill_set = models.TextField(max_length=900)
    personal_statement = models.TextField(max_length=2000)
    previous_work = models.TextField(max_length=2000)