from django.urls import path
from sim import views
from sim.views import (
    SimView,
    SimListView,
    InsertControl,
    TestView,
    DeleteTestView,
    ChartView,
    DeleteTramView, ModbusView)

app_name = 'sim'

urlpatterns = [
    path('',SimView.as_view(), name ='sim'),
    path('m',ModbusView.as_view(),name = 'modbus'),
    path('sl/',SimListView.as_view(), name ='sim_list'),
    path('control/',InsertControl.as_view()),
    path('test/',TestView.as_view()),
    path('delete/test',DeleteTestView),
    path('delete/tram',DeleteTramView),
    # path('delete/tram',DeleteTramView),
    # path('chart1/',ticket_class_view),
    # path('chart', 'chartFishPrice', name='chartFishPrice'),
]
