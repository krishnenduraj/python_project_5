from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('about/',views.about,name='about'),
    #path('add/',views.add,name='add'),
    #path('sub/',views.subtract,name='subtract'),
    #path('multiple/',views.multiple,name='multiple'),


]