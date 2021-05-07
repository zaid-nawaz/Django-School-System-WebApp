# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class schooldata(models.Model):
    schoolname = models.CharField(max_length=200)
    schoolpassword = models.CharField(max_length=200)
    schoolemail = models.CharField(max_length=200)
    schooldescription = models.TextField(max_length=3000)
    schoolnumber = models.IntegerField(default=0)
    schoolteacherkey = models.CharField(max_length=300)
    schoolstudentkey = models.CharField(max_length=300)

    def __str__(self):
        return self.schoolname