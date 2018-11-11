from django.urls import path
from station.views import (
    StationView, ControlView, ReportView,
    MapView,HealthyView,AlarmView,
    ParameterView, ModbusView,AccountView,
    GroupView,CreateView,GroupListView,TeView,LanguageView
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
    path('<int:pk>/account/', AccountView.as_view(),name ='tai-khoan'),
    path('<int:pk>/account/group/', GroupView.as_view(),name ='group'),
    path('<int:pk>/account/group/list', GroupListView.as_view(),name ='group-list'),
    path('<int:pk>/account/create/', CreateView.as_view(),name ='create'),
    path('<int:pk>/language/', LanguageView.as_view(),name ='language'),
    # path('data_ph/', pHView.as_view(),name =''),
    # path('data_clo/',CloView.as_view(),name =''),
    # path('data_tubi/', TubiView.as_view(),name =''),
]
