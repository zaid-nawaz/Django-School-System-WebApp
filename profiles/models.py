# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class studentprofile(models.Model):
    studentid = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=200)
    studentrollno = models.IntegerField(default=0)
    studentcontactno = models.IntegerField(default=0)
    studentpic = models.ImageField(upload_to='')
    studentclass = models.IntegerField(default=0)
    studentquote = models.CharField(max_length=30)
    studentachievements = models.TextField(max_length=3000)
    studentmothername = models.CharField(max_length=200)
    studentfathername = models.CharField(max_length=200)
    studentDescription = models.TextField(max_length=3000)
    studentPreviousYearsPercentage = models.CharField(max_length=30)
    profession = models.CharField(max_length=100,default='')
    studentrating = models.IntegerField(default=0)

    def __str__(self):
        return self.studentname

class teacherprofile(models.Model):
    teacherid = models.AutoField(primary_key=True)
    teachername = models.CharField(max_length=200)
    teachercontactno = models.IntegerField(default=0)
    teacherpic = models.ImageField(upload_to='')
    teacherclass = models.IntegerField(default=0)
    teacherquote = models.CharField(max_length=30)
    teacherqualifications = models.TextField(max_length=3000)
    teacherDescription = models.TextField(max_length=3000)
    profession = models.CharField(max_length=100,default='')
    teacherrating = models.IntegerField(default=0)

    def __str__(self):
        return self.teachername