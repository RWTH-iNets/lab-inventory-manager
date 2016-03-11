from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=1024)
    serial = models.CharField(max_length=1024)
    category = models.ManyToManyField(Category)
    location = models.CharField(max_length=1024, blank = True, null = True)
    img_url = models.CharField(max_length=1024, blank = True, null = True)
    doc_url = models.CharField(max_length=1024, blank = True, null = True)

    def __str__(self):
        return self.name

class SpectrumAnalyzer(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    input_power_max = models.IntegerField(blank = True, null = True)

class SignalGenerator(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)

class VectorSignalGenerator(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)

class ArbitaryWaveformGenerator(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)

class SoftwareDefinedRadio(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)

class Laptop(Item):
    pass

class NetworkAnalyzer(Item):
    pass

class Reservation(models.Model):
    reserved_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE)
    item = models.ForeignKey('manager.Item', on_delete=models.CASCADE)
    reserved_on = models.DateField()
    reserved_until = models.DateField()

class Inventory(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    count = models.IntegerField()
