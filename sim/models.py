import datetime
from django.db import models
from django.utils import timezone

from accounts.models import User

class Station(models.Model):
    display_name = models.CharField(max_length=50)
    symbol_name = models.CharField(max_length=50)
    serial = models.IntegerField()
    managed_by_users = models.ManyToManyField(User)
    def __str__(self):
        return self.display_name

class StationConfig(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=20)
    symbol_name = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)
    def __str__(self):
        return '%s - %s - %s' % (self.station, self.symbol_name, self.unit)


class StationConfigValue(models.Model):
    station_config = models.ForeignKey(StationConfig, on_delete=models.CASCADE)
    value = models.FloatField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)

    def station(self):
        return self.station_config.station

    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

    def ngaygio_int(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.timestamp()
        return format

class StationHealthy(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=20)
    symbol_name = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)
    def __str__(self):
        return '%s - %s - %s' % (self.station, self.symbol_name, self.unit)

class StationHealthyValue(models.Model):
    station_healthy = models.ForeignKey(StationHealthy, on_delete=models.CASCADE)
    value = models.FloatField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)

    def station(self):
        return self.station_healthy.station

    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

class Control(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    r1 = models.BooleanField()
    r2 = models.BooleanField()
    r3 = models.BooleanField()
    r4 = models.BooleanField()
    s1 = models.BooleanField()
    s2 = models.BooleanField()
    s3 = models.BooleanField()
    s4 = models.BooleanField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)

    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

class Modbus(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    BAUD_CHOICES = (
        ('0', '4800'),
        ('1', '9600'),
        ('2', '14400'),
        ('3', '19200'),
        ('4', '28800'),
        ('5', '38400'),
        ('6', '56000'),
        ('7', '57600'),
        ('8', '115200'),
        ('9', '128000'),
        ('A', '256000'),
    )
    baud_main = models.CharField(max_length=1,choices=BAUD_CHOICES,default='9')
    address_main = models.CharField(max_length=2)
    baud_subordinate = models.CharField(max_length=1,choices=BAUD_CHOICES,default='9')
    address_subordinate = models.CharField(max_length=2)
    address_resgiter_main = models.CharField(max_length=4)
    length_resgiter_main = models.CharField(max_length=4)
    upd = models.BooleanField(default=0)
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)


class Parameter(models.Model):
    TYPE_CHOICES = (
        ('2', 'Int'),
        ('4', 'Float'),
    )
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    symbol_name = models.CharField(max_length=20)
    start_address = models.IntegerField()
    type = models.CharField(max_length=1,choices=TYPE_CHOICES,default='2')
    scale = models.FloatField()
    unit = models.CharField(max_length=20)

class Status(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    sig = models.IntegerField()
    temp = models.FloatField()
    vol = models.FloatField()
    cnn = models.BooleanField()
    b = models.IntegerField()
    n = models.BooleanField()
    d = models.BooleanField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)
    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

class DailyRest(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    dr = models.IntegerField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)
    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

class CNE(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    cne = models.IntegerField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)
    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

class GPRS(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    gprs = models.IntegerField()
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)
    def ngaygio_ict(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return format

class Test(models.Model):
    test =  models.CharField(max_length=255)
    ngaygio = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        format = self.ngaygio + datetime.timedelta(hours=7)
        format = format.strftime("%H:%M:%S  %d-%m-%Y ")
        return '%s %s' % (self.test,format)



