# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class videolectures(models.Model):
    videoid = models.AutoField(primary_key=True)
    videoname = models.CharField(max_length=200)
    videothumbnail = models.ImageField(upload_to='')
    videoDescription = models.TextField(max_length=3000)
    videoSubject = models.CharField(max_length=200)
    videofile = models.FileField()

    def __str__(self):
        return self.videoname

class videocourses(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=200)
    coursedescription = models.TextField(max_length=3000)

    def __str__(self):
        return self.coursename