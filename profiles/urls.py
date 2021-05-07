from django.conf.urls import url , include
from profiles import views

urlpatterns = [

    url(r'^$',views.studentsprofilepage,name='studentsprofilepage'),
    url(r'^teachers/',views.teachersprofilepage,name='teachersprofilepage'),

]