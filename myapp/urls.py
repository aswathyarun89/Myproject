from django.urls import path
from . import views


urlpatterns = [
    path('Firstpgm', views.myfun,name='Firstpgm'),
    path('secpgm', views.fun,name='secpgm'),#
    path('mypgm', views.myfunction,name='mypgm')
 
]
