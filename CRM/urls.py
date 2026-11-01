from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('base',base,name='base'),
    path('details/<pk>',bannerDetails,name='bannerDetails'),
    path('Editdetails/<pk>',Editdetails,name='Editdetails'),
    path('detailsDelete/<pk>',detailsDelete,name='detailsDelete'),
    path('login/', auth_views.LoginView.as_view(template_name='CRM/login.html'), name='login'),
    path('registration/',register_request, name='registration'),
    path("student-search",studentsearch, name="student-search"),
]