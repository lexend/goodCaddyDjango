from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	caddy,
	quick_appointmnet,
	appointment_book,
	)

urlpatterns = [
    path('', views.caddy, name='caddy'),
    path('my_appointment/', views.caddy, name='caddy'),
    path('quick_appointmnet/', views.quick_appointmnet, name='quick_appointmnet'),
    path('update/<int:id>/', views.appointment_book,name='appointment_update'),

]
