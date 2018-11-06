from django.contrib import admin
from sim.models import (
    Station,
    StationConfig,
    StationConfigValue,
    StationHealthy,
    StationHealthyValue,
    Control,
    Test, Modbus, Parameter, DailyRest, GPRS, Status, CNE)


class StationConfigValueAdmin(admin.ModelAdmin):
    list_display = ['station', 'station_config', 'value', 'ngaygio_ict']
    list_filter = ['station_config__station']

class StationHealthyValueAdmin(admin.ModelAdmin):
    list_display = ['station', 'station_healthy', 'value', 'ngaygio_ict']
    list_filter = ['station_healthy__station']

class ModbusAdmin(admin.ModelAdmin):
    list_display = ['station','baud_master','address_master','address_resgiter_master','length_resgiter_master']
    # list_filter = ['station__station']

class ParameterAdmin(admin.ModelAdmin):
    list_display = ['station','symbol_name','start_address','type','scale','unit']

class DrAdmin(admin.ModelAdmin):
    list_display = ['station','dr','ngaygio_ict']

class GPRSAdmin(admin.ModelAdmin):
    list_display = ['station','gprs','ngaygio_ict']

class CneAdmin(admin.ModelAdmin):
    list_display = ['station','cne','ngaygio_ict']

class ControlAdmin(admin.ModelAdmin):
    list_display = ['station','r1','r2','s1','s2','ngaygio_ict']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['station','sig','cnn','temp','vol','ngaygio_ict']

admin.site.register(Station)
admin.site.register(StationConfig)
admin.site.register(StationConfigValue, StationConfigValueAdmin)
admin.site.register(StationHealthy)
admin.site.register(StationHealthyValue, StationHealthyValueAdmin)
admin.site.register(Control,ControlAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(DailyRest,DrAdmin)
admin.site.register(CNE,CneAdmin)
admin.site.register(Modbus,ModbusAdmin)
admin.site.register(Parameter,ParameterAdmin)
admin.site.register(GPRS,GPRSAdmin)
admin.site.register(Test)

