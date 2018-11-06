from sim.models import Station, StationConfig, StationConfigValue, Control
from rest_framework import routers, serializers, viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from sim.api.permission import IsOwnerOrReadOnly


# class StationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StationConfigValue
#         fields = ('station_config', 'value', 'ngaygio_ict')
#
# class StationViewSet(viewsets.ModelViewSet):
#     queryset = StationConfigValue.objects.order_by('-id')[:3]
#     serializer_class = StationSerializer

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationConfigValue
        fields = ('station_config', 'value', 'ngaygio_ict')

class StationListAPIView(ListAPIView):
    # station1 = Station.objects.get(sr=1)
    # station_config = StationConfig.objects.filter(station=station1,name='pH')
    queryset = StationConfigValue.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAuthenticated]

class StationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('station', 'r1', 'r2')

class StationDetailAPIView(RetrieveAPIView): # lookup_field = 'station' chi echo 1 obj
    # station1 = Station.objects.get(sr=1)
    # station_config = StationConfig.objects.filter(station=station1,name='pH')
    queryset = StationConfigValue.objects.all()
    serializer_class = StationDetailSerializer
    permission_classes = [IsAuthenticated]

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('station','r1', 'r2','s1','s2')

class ContListAPIView(ListAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    permission_classes = [IsAuthenticated]

class ContDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('station','r1', 'r2','s1','s2')

class ContDetailAPIView(RetrieveAPIView): # lookup_field = 'station' chi echo 1 obj
    queryset = Control.objects.all()
    serializer_class = ContDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'station'

# class ContUpdateAPIView(UpdateAPIView):
#     queryset = Control.objects.all()
#     serializer_class = ContDetailSerializer
#     lookup_field = 'station'
#
# class ContDeleteAPIView(DestroyAPIView):
#     queryset = Control.objects.all()
#     serializer_class = ContDetailSerializer
#     lookup_field = 'station'

# class pHSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StationConfigValue
#         fields = ('value', 'ngaygio_int')
#
# class pHViewSet(viewsets.ModelViewSet):
#     station1 = Station.objects.get(sr=1)
#     station_config = StationConfig.objects.get(station=station1,name='pH')
#     queryset = StationConfigValue.objects.filter(station_config=station_config)
#     serializer_class = pHSerializer
