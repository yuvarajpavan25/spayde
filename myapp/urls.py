from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('service/',Service,name='service'),
    path('contact/',Contact,name='contact'),
    path('location/',Location,name='location'),
    path('bookapp/',Bookapp,name='bookapp'),
    path('get_doctors/<str:category>/', views.get_doctors, name='get_doctors'),
    path('doctors/',doctor_list,name='doctors'),

]