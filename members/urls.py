from django.urls import path
from . import views

urlpatterns = [
     path('', views.main, name='main'),
     path('text/', views.display, name='mem'),
     path('inserting/', views.data_insertion, name= 'insert'),
     path('listing/', views.list_drink, name='list'),
     path('multiply/', views.product, name='multiplaying'),
     path('tabling/', views.all_member, name='table'),
     path('detailing/<id>/',views.members_details, name= 'detail'),
     #path('',views.debug),
     path('templating/', views.testing, name='templating'), 
     path('templating2/',views.testing2, name='templating2'),
     path('templating3/',views.testing3, name='template3'),
     path('reversing/', views.reversed_loop, name= 'reverse'),
     path('including',views.include, name= "include"),
     path('trying/',views.trying, name = 'try'),
     path('trying2/',views.trying2, name = 'try2'),
     path('filtering1', views.filter1, name = 'try3'),
     path('filtering/',views.filter, name='filter'),
     path('filtering2', views.filter2, name='filter22'),
     path('startingwith',views.startwith, name = 'startwi'),
     path('ordering/',views.order, name = 'ord'),
     path('reversedorder', views.descendingorder, name = 'reversed'),
     path('multipleorder', views.multipleOrder, name='')


] 
