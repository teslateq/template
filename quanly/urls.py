from django.urls import path, include
from quanly.views import AjaxStationDetailView, ManagerView, LanguageView

app_name = 'manager'

urlpatterns = [
    path('',ManagerView.as_view(), name ='manager'),
    path('ajax_station_detail/<int:pk>/', AjaxStationDetailView.as_view()),
    # path('language/', LanguageView.as_view(),name ='language'),
]
