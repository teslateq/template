from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from accounts.models import User
from project.models import Project
from sim.models import Station

class ManagerView(LoginRequiredMixin,TemplateView):
    login_url = '/account/'
    template_name = 'manager/manager.html'
    def get_context_data(self, **kwargs):
        context = super(ManagerView, self).get_context_data(**kwargs)
        context['stations'] = Station.objects.all()
        # context['project'] = Project.objects.all()
        p = Project.objects.all()
        context['project'] = p[0]
        return context

# class ReportView(LoginRequiredMixin,TemplateView):
#     login_url = '/account/'
#     template_name = 'manager/report.html'
#     def get_context_data(self, **kwargs):
#         context = super(ReportView, self).get_context_data(**kwargs)
#         id = self.request.GET['id']
#         station = Station.objects.get(id=id)
#         context['station'] = station
#         return context

class AjaxStationDetailView(LoginRequiredMixin,TemplateView):
    login_url = '/account/'
    template_name = 'manager/station_detail.html'
    def get_context_data(self, **kwargs):
        context = super(AjaxStationDetailView, self).get_context_data(**kwargs)
        # id = self.request.GET['id']
        station = Station.objects.get(pk = kwargs['pk'])
        context['station'] = station
        return context
#
# class ControlView(LoginRequiredMixin,TemplateView):
#     login_url = '/account/'
#     template_name = 'manager/control.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ReportView, self).get_context_data(**kwargs)
    #     id = self.request.GET['id']
    #     station = Station.objects.get(id=id)
    #     context['station'] = station
    #
    #     return context
