from django.urls import path
from station.views import (
    StationView, ControlView, ReportView,
    MapView,HealthyView,AlarmView,
    ParameterView, ModbusView
)
    # , ControlView, StationView ,ReportView
# from station.views.station_view import StationView
# from station.views.parameter_view import ParameterView
# from station.views.modbus_view import  ModbusView

app_name = 'station'

urlpatterns = [
    path('<int:pk>/giam-sat/', StationView.as_view(),name ='giam-sat'),
    path('<int:pk>/bao-cao/',ReportView.as_view(),name ='bao-cao'),
    path('<int:pk>/dieu-khien/',ControlView.as_view(),name ='dieu-khien'),
    path('<int:pk>/ban-do/',MapView.as_view(),name ='ban-do'),
    path('<int:pk>/suc-khoe/',HealthyView.as_view(),name ='suc-khoe'),
    path('<int:pk>/canh-bao/',AlarmView.as_view(),name ='canh-bao'),
    path('<int:pk>/parameter/',ParameterView.as_view(),name ='parameter'),
    path('<int:pk>/modbus/', ModbusView.as_view(),name ='modbus'),
]
