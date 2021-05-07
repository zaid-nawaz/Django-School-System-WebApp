from django.shortcuts import render
from videolectures.models import videocourses
def index(request):
    firstrow = videocourses.objects.all()[0:3]
    secondrow = videocourses.objects.all()[3:5]
    thirdrow = videocourses.objects.all()[5:8]
    params = {
        'firstrow':firstrow,
        'secondrow':secondrow,
        'thirdrow':thirdrow,
    }
    return render(request,'schoolsystem/index.html',params)