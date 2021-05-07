# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from videolectures.models import videolectures,videocourses
# Register your models here.
admin.site.register(videolectures)
admin.site.register(videocourses)