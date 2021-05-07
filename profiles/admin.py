# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from profiles.models import studentprofile,teacherprofile
# Register your models here.
admin.site.register(studentprofile)
admin.site.register(teacherprofile)