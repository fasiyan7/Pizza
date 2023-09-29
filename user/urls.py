
from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
#path('',views.show,name='show'),

path('',views.show, name='show'),
path('register', views.signupView),

]
