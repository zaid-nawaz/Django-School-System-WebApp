# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect,redirect
from signuplogin.models import schooldata
import random
import string
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from profiles.models import teacherprofile,studentprofile
# Create your views here.

# def generate_key(length):
#     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
# good way of generating key

def loginpage(request):
    if request.method == 'POST':
        loginname = request.POST['Loginname']
        loginpassword = request.POST['Loginpassword']
        usser = authenticate(username=loginname,password=loginpassword)
        if usser is not None:
            login(request,usser)
            print('successfully logged in')
            return HttpResponseRedirect('/')
        else:
            print('not hello')

    return render(request,'signuplogin/loginpage.html')

def handlelogout(request):
    logout(request)
    print('logged out')
    return HttpResponseRedirect('/authentications/login/')

def signuppage(request):
    signname = request.GET['signname']
   
    
    if request.method == 'POST' and signname=='school':
        schoolname = request.POST['name']
        schoolpassword =  request.POST['password']
        schoolemail =  request.POST['emailaddress']
        schooldescription =  request.POST['schooldescription']
        schoolnumber =  request.POST['phonenumber']
        Teacherkey = os.urandom(12).encode('hex')
        Studentkey = os.urandom(12).encode('hex')
        sch = schooldata(schoolname=schoolname,schoolpassword=schoolpassword,schoolemail=schoolemail,schooldescription=schooldescription,schoolnumber=schoolnumber,schoolteacherkey=Teacherkey,schoolstudentkey=Studentkey)
        sch.save()

 
       
        params ={
            'success':True,
            'teacherkey':Teacherkey,
            'studentkey':Studentkey,
        }
        return render(request,'signuplogin/schoolsignup.html',params)

    if request.method == 'POST' and signname=='teacher':
        teachername = request.POST['name']
        teacherpassword =  request.POST['password']
        teacheremail =  request.POST['emailaddress']
        teacherpic = request.POST['teacherpic']
        teacherclassno = request.POST['classno']
        teacherquote = request.POST['quote']
        teacherdescription =  request.POST['teacherdesc']
        teacherqual =  request.POST['teacherqual']
        teachernumber =  request.POST['phonenumber']
        teacherkey = request.POST['key']
        teacherschoolname = request.POST['schoolname']
        
        if schooldata.objects.filter(schoolname=teacherschoolname):
            if schooldata.objects.filter(schoolname=teacherschoolname)[0].schoolteacherkey == teacherkey:
                teacheruser = User.objects.create_user(teachername,teacheremail,teacherpassword)
                teacheruser.save()
                teacheruserprofile = teacherprofile(teachername=teachername,teachercontactno=teachernumber,teacherpic=teacherpic,teacherclass=teacherclassno,teacherquote=teacherquote,teacherqualifications=teacherqual,teacherDescription=teacherdescription,profession='teacher')
                teacheruserprofile.save()
                return HttpResponseRedirect('/')


            else:
                print('this is not me')
            


       
        # params ={
        #     'success':True,
        #     'teacherkey':Teacherkey,
        #     'studentkey':Studentkey,
        # }
        return render(request,'signuplogin/schoolsignup.html')

    if request.method == 'POST' and signname=='student':
        studentname = request.POST['name']
        studentpassword =  request.POST['password']
        studentemail =  request.POST['emailaddress']
        studentpic = request.FILES['studentpic']
        studentclassno = request.POST['classno']
        studentquote = request.POST['quote']
        studentrollno = request.POST['rollno']
        studentfathername = request.POST['fathername']
        studentmothername = request.POST['mothername']
        studentprevyearpercentage = request.POST['prevyearpercent']
        studentachievements = request.POST['studentachievements']
        studentdescription =  request.POST['studentdescription']
        studentnumber =  request.POST['phonenumber']
        studentkey = request.POST['key']
        studentschoolname = request.POST['schoolname']
        
        if schooldata.objects.filter(schoolname=studentschoolname):
            if schooldata.objects.filter(schoolname=studentschoolname)[0].schoolstudentkey == studentkey:
                studentuser = User.objects.create_user(studentname,studentemail,studentpassword)
                studentuser.save()
                studentuserprofile = studentprofile(studentname=studentname,studentrollno=studentrollno,studentcontactno=studentnumber,studentpic=studentpic,studentclass=studentclassno,studentquote=studentquote,studentachievements=studentachievements,studentDescription=studentdescription,profession='student',studentfathername=studentfathername,studentmothername=studentmothername,studentPreviousYearsPercentage=studentprevyearpercentage)
                studentuserprofile.save()
                return HttpResponseRedirect('/')


            else:
                print('this is not me')
            


       
        # params ={
        #     'success':True,
        #     'teacherkey':Teacherkey,
        #     'studentkey':Studentkey,
        # }
        return render(request,'signuplogin/schoolsignup.html')
    

    if signname == 'teacher':
        return render(request,'signuplogin/teachersignup.html')
    elif signname == 'school':
        return render(request,'signuplogin/schoolsignup.html')
    elif signname == 'student':
        return render(request,'signuplogin/studentsignup.html')


def signupforall(request):
    return render(request,'signuplogin/signupforall.html')