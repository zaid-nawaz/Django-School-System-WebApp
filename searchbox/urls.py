from django.conf.urls import url , include
from searchbox import views


urlpatterns = [

    url(r'^$',views.searchindex,name='searchindex'),
    url(r'^searchresults/',views.searchresults,name='searchresults'),
    url(r'^allresults/',views.allresults,name='allresults')

]