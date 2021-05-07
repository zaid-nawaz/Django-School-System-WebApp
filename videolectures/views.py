# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from videolectures.models import videolectures,videocourses
import socket
import time
# Create your views here.
def videosearch(request):
    if request.method == 'POST':
        queryname = request.POST['queryname']
        obje = videocourses.objects.filter(coursename=queryname)
        if len(obje) == 0:
            print('sorry')
        else:
            params = {'obj':obje}
            return render(request,'videolectures/index.html',params)

    obj = videocourses.objects.all()[0:3]
  
       
    params = {'obj':obj}
    return render(request,'videolectures/index.html',params)

def videolists(request):
    query = request.GET['sub']

   
    obj = videolectures.objects.filter(videoSubject=query)
    objs  = videocourses.objects.all()
    objss = list(objs)
    for i in objss:
        if i.coursename == query:
            objss.remove(i)

  
    params = {'obj':obj,'objs':objss[0:6]}
    
    return render(request,'videolectures/videolist.html',params)
    