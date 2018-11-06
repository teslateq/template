from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from project.models import Project
from sim.models import Station, StationConfigValue, StationConfig, Control


class StationView(TemplateView):
    template_name = 'station/station.html'
    def get_context_data(self, **kwargs):
        context = super(StationView, self).get_context_data(**kwargs)
        self.request.session['id_station'] = kwargs['pk']
        tes = self.request.session.get('id_station')
        if Station.objects.filter(pk = tes).exists():
            context['stations'] = Station.objects.get(pk = kwargs['pk'])
        else:
            context['err'] = "k ton tai"
        p = Project.objects.all()
        context['project'] = p[0]
        return context

class HealthyView(TemplateView):
    template_name = 'station/healthy.html'
    def get_context_data(self, **kwargs):
        context = super(HealthyView, self).get_context_data(**kwargs)
        self.request.session['id_station'] = kwargs['pk']
        tes = self.request.session.get('id_station')
        if Station.objects.filter(pk = tes).exists():
            context['stations'] = Station.objects.get(pk = kwargs['pk'])
        else:
            context['err'] = "k ton tai"
        p = Project.objects.all()
        context['project'] = p[0]
        return context
# class ReportView(LoginRequiredMixin,ListView):
#     login_url = '/account/'
#     template_name = 'station/report.html'
#     paginate_by = 10
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = StationConfigValue.objects.all()
#         return context
    # context_object_name = 'data'
    # station = Station.objects.get(pk = 1)
    # config = StationConfig.objects.filter(station=station)
    # queryset = StationConfigValue.objects.all(station_config = config)
    # def get_context_data(self, **kwargs):
    #     context = super(ReportView, self).get_context_data(**kwargs)
    #     context['stations']  = StationConfig.objects.all()
    #     return context

class ReportView(LoginRequiredMixin,TemplateView):
    login_url = '/account/'
    template_name = 'station/report.html'
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['stations'] = Station.objects.get(pk = kwargs['pk'])
        context['station']  = Station.objects.get(pk = kwargs['pk'])
        p = Project.objects.all()
        context['project'] = p[0]
        return context



class ControlView(LoginRequiredMixin,TemplateView):
    login_url = '/account/'
    template_name = 'station/control.html'
    def get_context_data(self, **kwargs):
        context = super(ControlView, self).get_context_data(**kwargs)
        # station = Station.objects.get(pk=kwargs['pk'])
        context['stations'] = Station.objects.get(pk = kwargs['pk'])
        context['control']  = Control.objects.get(station=context['stations'])
        p = Project.objects.all()
        context['project'] = p[0]
        return context



class MapView(LoginRequiredMixin,TemplateView):
    login_url = '/account/'
    template_name = 'station/map.html'
    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['station']  = Station.objects.get(pk = kwargs['pk'])
        p = Project.objects.all()
        context['project'] = p[0]
        return context

class AlarmView(TemplateView):
    template_name = 'station/alarm.html'
    def get_context_data(self, **kwargs):
        context = super(AlarmView, self).get_context_data(**kwargs)
        self.request.session['id_station'] = kwargs['pk']
        tes = self.request.session.get('id_station')
        if Station.objects.filter(pk = tes).exists():
            context['stations'] = Station.objects.get(pk = kwargs['pk'])
        else:
            context['err'] = "k ton tai"
        p = Project.objects.all()
        context['project'] = p[0]
        return context

class ParameterView(TemplateView):
    template_name = 'station/parameter.html'
    def get_context_data(self, **kwargs):
        context = super(ParameterView, self).get_context_data(**kwargs)
        self.request.session['id_station'] = kwargs['pk']
        tes = self.request.session.get('id_station')
        if Station.objects.filter(pk = tes).exists():
            context['stations'] = Station.objects.get(pk = kwargs['pk'])
        else:
            context['err'] = "k ton tai"
        p = Project.objects.all()
        context['project'] = p[0]
        return context

class ModbusView(TemplateView):
    template_name = 'station/modbus.html'
    def get_context_data(self, **kwargs):
        context = super(ModbusView, self).get_context_data(**kwargs)
        self.request.session['id_station'] = kwargs['pk']
        tes = self.request.session.get('id_station')
        if Station.objects.filter(pk = tes).exists():
            context['stations'] = Station.objects.get(pk = kwargs['pk'])
        else:
            context['err'] = "k ton tai"
        p = Project.objects.all()
        context['project'] = p[0]
        return context

# class StationView(TemplateView):
#     template_name = 'station/station.html'
