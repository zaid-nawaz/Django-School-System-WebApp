from django.conf.urls import url , include
from videolectures import views


urlpatterns = [

    url(r'^$',views.videosearch,name='videosearch'),
    url(r'^videolists/',views.videolists,name='videolists')

]