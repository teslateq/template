from django.urls import path
from sim import views
from sim.api.views import ContListAPIView, ContDetailAPIView, StationListAPIView

urlpatterns = [
    path('control/',ContListAPIView.as_view(), name ='cont-api'),
    path('control/<int:station>/',ContDetailAPIView.as_view(), name ='cont-detail-api'),
    path('station/',StationListAPIView.as_view(), name ='cont-api'),
    # path('sl/',SimListView.as_view(), name ='sim_list'),
    # path('control',InsertControl.as_view()), <int:pk>/
]
