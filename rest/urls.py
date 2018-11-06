from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from accounts.models import User
# from sim.api.views import StationViewSet, ContListAPIView


# , pHViewSet


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'tram', StationViewSet)
# router.register(r'control', ContListAPIView)
# router.register(r'pH', pHViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
