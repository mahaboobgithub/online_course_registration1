from django.db import models

# Create your models here.
from django.db import models


class Coursemodel(models.Model):
    course_name = models.CharField(primary_key=True, unique=True, max_length=50)
    faculty = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    fee = models.FloatField(max_length=10)
    duration = models.IntegerField()


class Studentmodel(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField(primary_key=True, unique=True)
    emailid = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    student_course = models.ManyToManyField(Coursemodel)


