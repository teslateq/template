import json

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseForbidden,HttpResponse,HttpResponseRedirect
from sim.models import (
    Station,
    StationConfig,
    StationConfigValue,
    Control,
    Test,
    StationHealthy,
    StationHealthyValue,
    Modbus, Status, DailyRest, GPRS)


# from django.core import serializers
# from rest_framework import routers, serializers, viewsets
# from rest_framework.generics import ListAPIView

class SimView(TemplateView):
    template_name = 'sim/sim.html'
    def get_context_data(self, **kwargs):
        context = super(SimView, self).get_context_data(**kwargs)
        sr = self.request.GET['sr']
        ph = self.request.GET['ph']
        clo = self.request.GET['clo']
        tubi = self.request.GET['tubi']
        # tem = self.request.GET['tem']
        # vol = self.request.GET['vol']
        if sr is not None :
            station1 = Station.objects.get(serial=sr)
            if ph is not None :
                station_config = StationConfig.objects.get(station=station1, symbol_name='ph')
                StationConfigValue.objects.create(station_config=station_config, value=ph)
            if clo is not None :
                station_config = StationConfig.objects.get(station=station1, symbol_name='clo')
                StationConfigValue.objects.create(station_config=station_config, value=clo)
            if tubi is not None :
                station_config = StationConfig.objects.get(station=station1, symbol_name='tubi')
                StationConfigValue.objects.create(station_config=station_config, value=tubi)
            # if vol is not None :
            #     station_config = StationHealthy.objects.get(station=station1, symbol_name='vol')
            #     StationHealthyValue.objects.create(station_healthy=station_config, value=vol)
            # if tem is not None :
            #     station_config = StationHealthy.objects.get(station=station1, symbol_name='temp')
                # StationHealthyValue.objects.create(station_healthy=station_config, value=tem)

            context['control'] = Control.objects.get(station=station1)
            return context
#
class ModbusView(TemplateView):
    template_name = 'sim/modbus.html'
    def get_context_data(self, **kwargs):
        context = super(ModbusView, self).get_context_data(**kwargs)
        sr = self.request.GET['sr']
        sig = self.request.GET['sig']
        dr = self.request.GET['dr']
        gprs = self.request.GET['gprs']
        cnn = self.request.GET['cnn']
        b = self.request.GET['b']
        h = self.request.GET['h']
        trh = self.request.GET['trh']
        sbaud = self.request.GET['sbaud']
        sadd = self.request.GET['sadd']
        mbaud = self.request.GET['mbaud']
        madd = self.request.GET['madd']
        trh = self.request.GET['trh']
        s = self.request.GET['s']
        d = self.request.GET['d']
        station = Station.objects.get(serial=sr)
        status = Station.objects.get(station=station)
        status.sig = sig
        DailyRest.objects.create(station=station,dr=dr)
        GPRS.objects.create(station=station,gprs=gprs)
        # CNE.objects.create(station=station,cne=cne)
        # if( b=='true'):
        # Status.objects.get(station=station)
        # Station.n = 0
        # c =.objects.get(station=station)
        # if(val=='true'):
        #         c.r2 = True
        #     else:
        #         c.r2 = False
        # c.save()
        m = Modbus.objects.all()
        if(m[0].upd == True):
            context['upd'] = 1
        if(m[0].upd == False):
            context['upd'] = 0
        context['baud_master'] = m[0].baud_master
        context['address_master'] = m[0].address_master
        context['baud_slave'] = m[0].baud_slave
        context['address_slave'] = m[0].address_slave
        context['address_resgiter_master'] = m[0].address_resgiter_master
        context['length_resgiter_master'] = m[0].length_resgiter_master
        status = Status.objects.all()
        if(status[0].cnn == True):
            context['cnn'] = 1
        if(status[0].cnn == False):
            context['cnn'] = 0
        if(status[0].n == True):
            context['n'] = 1
        if(status[0].n == False):
            context['n'] = 0
        if(status[0].d == True):
            context['d'] = 1
        if(status[0].d == False):
            context['d'] = 0

        c = Control.objects.get(station=station)
        if(c.r1 == True):
            context['r1'] = 1
        if(c.r1 == False):
            context['r1'] = 0
        if(c.r2 == True):
            context['r2'] = 1
        if(c.r2 == False):
            context['r2'] = 0
        return context

    # address_master = models.CharField(max_length=2)
    # address_resgiter_master = models.CharField(max_length=4)
    # length_resgiter_master

# def index(request):
#     m = ModbusRTU.objects.all()
#     context = {'modbus': m[0].baud_master}
#     return render(request, 'sim/modbus.html', context)

class SimListView(TemplateView):
    template_name = 'sim/sim.html'
    def get_context_data(self, **kwargs):
        context = super(SimListView, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        station = Station.objects.get(id=id)
        context['stations'] = station
        return context

# class SimListView(ListView):
#     model = Station
#     template_name = 'sim/sim.html'
#     context_object_name = 'stations'
#
#     def get_queryset(self):
#         return Station.objects.all()


# class AjaxStationDetailView(TemplateView):
#     template_name = 'sim/station_detail.html'
#
# def get_context_data(self, **kwargs):
#     context = super(AjaxStationDetailView, self).get_context_data(**kwargs)

    #context['station'] = station
    #return station

# class StationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StationConfigValue
#         fields = ('station_config', 'value', 'ngaygio_ict')
#
# class StationViewSet(viewsets.ModelViewSet):
#     queryset = StationConfigValue.objects.order_by('-id')[:3]
#     serializer_class = StationSerializer
#
# class ControlSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Control
#         fields = ('station', 'r1', 'r2')
#
# class ControlViewSet(viewsets.ModelViewSet):
#     queryset = Control.objects.all()
#     serializer_class = ControlSerializer
#
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

class InsertControl(TemplateView):
    template_name = 'sim/sim.html'
    def get_context_data(self, **kwargs):
        context = super(InsertControl, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        dk = self.request.GET['dk']
        val = self.request.GET['val']
        station = Station.objects.get(id=id)
        control=Control.objects.get(station=station)
        if(dk == 'dk1'):
            if(val=='true'):
                control.r1 = True
            else:
                control.r1 = False
        else:
            if(val=='true'):
                control.r2 = True
            else:
                control.r2 = False
        control.save()
        # context['stations'] = station
        # return context


class TestView(TemplateView):
    template_name = 'sim/sim.html'
    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        test = self.request.GET['test']
        Test.objects.create(test=test)
        test = Test.objects.latest('test')
        context['test'] = test
        return context

def DeleteTestView(request):
    Test.objects.all().delete()
    context= {}
    return render(request, 'sim/sim.html', context)

def DeleteTramView(request):
    StationConfigValue.objects.all().delete()
    StationHealthyValue.objects.all().delete()
    context= {}
    return render(request, 'sim/sim.html', context)

class ChartView(TemplateView):
    template_name = 'sim/chart.html'

# def chartFishPrice(request):
#     ff = Data.objects.all()
#     data = []
#     for f in ff:
#         da = {}
#         da['ngay'] = f.ngaygio
#         da['value'] = f.value
#         data.append(da)

    # thumbnail_list = []
    # for file in media:
    # file_info = {}
    # file_info['url'] = file.url
    # file_info['title'] = file.title
    # thumbnail_list.append(file_info)

    # for f in ff:
    #     data['dates'].append(int(f.ngaygio.strftime("%s")))
    #     data['values'].append(int(f.value))
    # data2 = {}
    # data2['chart_data'] = data
    # print data2
