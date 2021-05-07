# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from profiles.models import studentprofile,teacherprofile
from itertools import chain
# Create your views here.
def searchindex(request):
    if request.method == 'POST':
        classno = request.POST.get('selecttheclass','')
        personname = request.POST.get('selecttheperson','')
        if personname == 'student':
            res = studentprofile.objects.filter(studentclass=classno)
            # params = {'stud':res}
            # return render(request,'searchbox/searchresults.html',params)
            if res.exists():
                params = {'stud':res}
                return render(request,'searchbox/searchresults.html',params)
            else:
                params = {'notexist':True}
                return render(request,'searchbox/searchresults.html',params)
        else:
            res = teacherprofile.objects.filter(teacherclass=classno)
            if res.exists():
                params = {'tech':res}
                return render(request,'searchbox/searchresults.html',params)
            else:
                params = {'notexist':True}
                return render(request,'searchbox/searchresults.html',params)
            # return render(request,'searchbox/searchresults.html',params)
    return render(request,'searchbox/index.html')

# def searchqueries(query,item):
#     if query.lower() in item.studentname.lower():
#         return True
#     else:
#         return False

def searchresults(request):
    if request.method == 'POST':
        searchquery = request.POST.get('queryname','')
        
        stu = studentprofile.objects.filter(studentname=searchquery.lower())
        tec = teacherprofile.objects.filter(teachername=searchquery.lower())
        stutec = list(chain(stu,tec))
        # stu = studentprofile.objects.all()
        # tec = teacherprofile.objects.all()
        # stutec = list(chain(stu,tec))
        # newstutec = []
        # for index,item in enumerate(stutec):
        #     if searchqueries(searchquery,stutec[index]):
        #         newstutec.append(item)
        print(stutec)
        if len(stutec) != 0:
            params = {'ses':stutec}
            print('ok')
            return render(request,'searchbox/searchresults.html',params)
        else:
            params = {'notexist':True}
            print('nothing')
            return render(request,'searchbox/searchresults.html',params)
    return render(request,'searchbox/searchresults.html')

def allresults(request):
    classno = request.GET.get('classno','')
    stu = studentprofile.objects.filter(studentclass=classno)
    params = {'stutech':stu}
    return render(request,'searchbox/searchresults.html',params)