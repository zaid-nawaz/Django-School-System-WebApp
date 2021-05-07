from django.conf.urls import url , include
from signuplogin import views

 
urlpatterns = [

    url(r'^$',views.signupforall,name='signupforall'),
    url(r'^login/',views.loginpage,name='loginpage'),
    url(r'^signup/',views.signuppage,name='signuppage'),
    url(r'^logout/',views.handlelogout,name='handlelogout'),
 

]