# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from profiles.models import studentprofile,teacherprofile


# Create your views here

def insert_str(string,str_to_insert,index):
    return string[:index] + str_to_insert + string[index:]

def studentsprofilepage(request):
    a = 32
    studid = request.GET['studid']
    studinfo = studentprofile.objects.filter(studentid=studid)
    studachieve = studinfo[0].studentachievements.split('.')[0:4]
    for index,achieve in enumerate(studachieve):
        if len(achieve) > a:
            x = insert_str(achieve,'\n',a)
            studachieve[index] = x
    studpercent = studinfo[0].studentPreviousYearsPercentage.split(',')
  
    studprevclass = studinfo[0].studentclass - 7
    leftrating = 5 - studinfo[0].studentrating

    allstud = studentprofile.objects.filter(studentrating=studinfo[0].studentrating)
    allstud = list(allstud)
    for index,item in enumerate(allstud):
        if allstud[index] == studinfo[0]:
            allstud.remove(item)
        
    listforratings = []
    for index,item in enumerate(allstud):
        x = allstud[index].studentrating
        listforratings.append(x)
    #i havent used this listforratings anywhere.

    params = {
        
        
        'studinfo':studinfo[0],
        'studachieve':studachieve,
        'studprevpercent':studpercent,
        'studprevclass':studprevclass,
        'student':True,
        'n':range(studinfo[0].studentrating),
        'leftrating':range(leftrating),
        'allstud':allstud,
        'listforratings':listforratings
        }
    return render(request,'profiles/index.html',params)

def teachersprofilepage(request):
    a = 32
    techid = request.GET['techid']
    techinfo = teacherprofile.objects.filter(teacherid=techid)
    techqual = techinfo[0].teacherqualifications.split('.')[0:4]
    for index,qual in enumerate(techqual):
        if len(qual) > a:
            x = insert_str(qual,'\n',a)
            techqual[index] = x
    leftrating = 5 - techinfo[0].teacherrating
    
    alltech = teacherprofile.objects.filter(teacherrating=techinfo[0].teacherrating)
    alltech = list(alltech)
    for index,item in enumerate(alltech):
        if alltech[index] == techinfo[0]:
            alltech.remove(item)

    params = {
        
        
        'techinfo':techinfo[0],
        'techqual':techqual,
        'student':False,
        'n':range(techinfo[0].teacherrating),
        'leftrating':range(leftrating),
        'alltech':alltech
        }
    return render(request,'profiles/teacher.html',params)
