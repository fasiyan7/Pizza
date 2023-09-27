
from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
#path('',views.show,name='show'),

path('<int:pid>',views.index, name='pizza'),
]
