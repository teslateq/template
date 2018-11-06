from django.urls import path, include
from quanly.views import  AjaxStationDetailView, ManagerView

app_name = 'manager'

urlpatterns = [
    path('',ManagerView.as_view(), name ='manager'),
    path('ajax_station_detail/<int:pk>/', AjaxStationDetailView.as_view()),

]
