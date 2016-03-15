from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Item(models.Model):
    serial = models.CharField(max_length=1024)
    location = models.CharField(max_length=1024, blank = True, null = True)
    notes = models.CharField(max_length=1024, blank = True, null = True)
    item_desc = models.ForeignKey('manager.ItemDescriptor', on_delete=models.CASCADE)

    def __str__(self):
        return self.serial

class ItemDescriptor(models.Model):
    name = models.CharField(max_length=1024)
    img_url = models.CharField(max_length=1024, blank = True, null = True)
    doc_url = models.CharField(max_length=1024, blank = True, null = True)
    category = models.ForeignKey('manager.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SpectrumAnalyzer(ItemDescriptor):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    input_power_max = models.IntegerField(blank = True, null = True)

class Oscilloscope(ItemDescriptor):
    bw = models.IntegerField(blank = True, null = True)
    samp_rate = models.IntegerField(blank = True, null = True)
    num_chan = models.IntegerField(blank = True, null = True)

class SignalGenerator(ItemDescriptor):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)

class USRP_Daughterboard(ItemDescriptor):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)
    input_power_max = models.IntegerField(blank = True, null = True)
    bw_max = models.IntegerField(blank = True, null = True)

class NetworkAnalyzer(ItemDescriptor):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)

class Reservation(models.Model):
    reserved_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE)
    item = models.ForeignKey('manager.Item', on_delete=models.CASCADE)
    reserved_from = models.DateTimeField()
    reserved_until = models.DateTimeField()

class ErrorReport(models.Model):
    item = models.ForeignKey('manager.Item', on_delete=models.CASCADE)
    desc = models.TextField()
    reported_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank = True, null = True)
    reported_on = models.DateTimeField()    
