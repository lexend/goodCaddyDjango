from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	golfer,
	golfer_appointment_list,
	appointment_delete,
	golfer_appointment_update,
	)





urlpatterns = [
    path('', views.golfer, name='golfer_home'),
    path('my_appointment/', views.golfer, name='golfer_appointment'),
    path('create_appointment/', views.golfer_appointment_list, name='golfer_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', golfer_appointment_update,name='golfer_appointment_update'),

]
